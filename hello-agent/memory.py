# @Version :1.0
# @Author  :TonyLai
# @File    :memory.py
# @Time    :2025/11/16 16:22

from typing import List, Dict, Any, Optional

class Memory:
    def __init__(self):
        self.records: List[Dict[str, Any]] = []

    def add_record(self , record_type : str, content : str):
        '''
        向记忆中添加一条新的记录
        :param record_type:  记录的类型（execution 或 reflection）
        :param content: 记录的具体内容：生成的代码或者返回反馈
        :return:
        '''
        record = {"type":record_type, "content": content}
        self.records.append(record)

        print(f"记忆已更新，新增一条:{content} 记录")

    def get_trajectory(self) -> str:
        '''
        核心代码：将记忆轨迹"序列化"成一段文本，可以直接插入到后续的提示词中，为模型的反思和优化提供完整的上下文
        将所有的记忆记录化为一个连贯的字符串文本，用于构建提示词
        :return:
        '''
        trajectory_parts = []
        for record in self.records:
            if record['type'] == 'execution':
                trajectory_parts.append(f"---上一轮尝试(代码)----\n{record['content']}")
            elif record['type'] == 'reflection':
                trajectory_parts.append(f"---评审员反馈---\n {record['content']}")
        return "\n\n".join(trajectory_parts)

    def get_last_execution(self)->Optional[str]:
        '''
        获取最近一次的执行结果，加入不存在在返回None
        :return:
        '''
        for record in reversed(self.records):
            if record['type'] == 'execution':
                return record['content']
        return None