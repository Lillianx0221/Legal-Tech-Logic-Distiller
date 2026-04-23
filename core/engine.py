import yaml
import time

class LegalSkillEngine:
    def __init__(self, skill_path, guardrail):
        with open(skill_path, 'r', encoding='utf-8') as f:
            self.skill_data = yaml.safe_load(f)
        self.guardrail = guardrail

    def process(self, task):
        # 1. 伦理核验
        safe, message = self.guardrail.validate_instruction(task)
        if not safe:
            return message

        # 2. 模拟逻辑解构过程
        print(f"\n> 正在调用逻辑模组: {self.skill_data['name']}...")
        time.sleep(0.5)
        
        output = "【逻辑执行成功】\n"
        output += "------------------------------------------\n"
        output += "当前思维链路 (CoT):\n"
        for idx, step in enumerate(self.skill_data['logic_paradigm']['thinking_process'], 1):
            output += f"{idx}. {step}\n"
        
        output += f"\n[任务响应]: 已根据法律科技实习生范式对 '{task}' 进行初步解析。\n"
        output += f"建议关注：{', '.join(self.skill_data['knowledge_mapping'] if 'knowledge_mapping' in self.skill_data else ['合规性', '算法鲁棒性'])}。\n"
        output += "------------------------------------------\n"
        output += self.skill_data['interaction_constraints']['disclaimer']
        
        return output
