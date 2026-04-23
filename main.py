from core.philosophy import EthicalGuardrail
from core.engine import LegalSkillEngine
import sys

def run():
    # 初始化
    guardrail = EthicalGuardrail()
    try:
        engine = LegalSkillEngine('skills/legal_intern_v1.yaml', guardrail)
    except FileNotFoundError:
        print("错误：未找到 skills/legal_intern_v1.yaml 文件。")
        return

    print("==========================================")
    print("   ⚖️ Legal-Tech Methodology Distiller   ")
    print("==========================================")
    print(guardrail.disclaimer)

    while True:
        try:
            user_task = input("\n请输入法律/技术分析任务 (输入 'exit' 退出): ")
            if user_task.lower() in ['exit', 'quit']:
                print("程序已安全关闭。")
                break
            
            if not user_task.strip():
                continue

            result = engine.process(user_task)
            print(result)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    run()
