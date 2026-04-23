"""
Legal Logic Distiller - Ethical Guardrails
"""

class EthicalGuardrail:
    def __init__(self):
        self.disclaimer = (
            "\n[系统提示]：已加载《法律科技方法论封装协议》。\n"
            "本模型严格遵循‘非人格化’原则，仅承载逻辑范式，不承载人类意识。\n"
        )

    def validate_instruction(self, user_input: str):
        """
        拦截具有‘黑镜’特征的剥削性或物化人类的指令。
        """
        forbidden_keywords = ["囚禁", "折磨", "奴役", "数字生命", "剥夺权利", "永恒工作"]
        for keyword in forbidden_keywords:
            if keyword in user_input:
                return False, "❌ 错误：输入包含违反《数字伦理红线》的内容。本系统拒绝将人‘物化’。"
        return True, None
