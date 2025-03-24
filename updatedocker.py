import requests
from bs4 import BeautifulSoup
import json
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        # 目标URL
        url = "https://www.coderjia.cn/archives/dba3f94c-a021-468a-8ac6-e840f85867ea"
        
        # 获取网页内容，指定UTF-8编码
        logging.info("正在获取网页内容...")
        response = requests.get(url)
        response.encoding = 'utf-8'
        
        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 找到第一个表格
        table = soup.find('table')
        if not table:
            raise ValueError("未找到表格")
            
        # 获取表头
        headers = [th.text.strip() for th in table.find_all('th')]
        
        # 提取数据
        data = {"registry-mirrors":[]}
        for row in table.find_all('tr')[1:]:  # 跳过表头
            cols = row.find_all('td')
            if len(cols) >= 2:  # 确保有至少两列
                row_data = {
                    "URL": cols[0].text.strip(),
                    "STATUS": cols[1].text.strip()
                }
                # 过滤"正常"或"新增"的行
                if row_data["STATUS"] in ['正常', '新增']:
                    data["registry-mirrors"].append(row_data["URL"])
        
        # 保存为JSON文件，使用UTF-8编码
        output_file = '/etc/docker/daemon.json'
        with open(output_file, 'w+', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        
        logging.info(f"成功保存{len(data['registry-mirrors'])}行数据到{output_file}")
        
    except Exception as e:
        logging.error(f"发生错误: {str(e)}")

if __name__ == "__main__":
    main()
