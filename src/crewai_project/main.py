#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crewai_project.crew import MyCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    运行 Crew
    """
    inputs = {"project_name": "AI 助手", "current_year": str(datetime.now().year)}

    try:
        MyCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"运行 Crew 时发生错误: {e}")


def train():
    """
    训练 Crew 若干轮次
    """
    inputs = {"project_name": "AI 助手", "current_year": str(datetime.now().year)}
    try:
        MyCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"训练 Crew 时发生错误: {e}")


def replay():
    """
    从指定任务重新播放 Crew 执行过程
    """
    try:
        MyCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"重放 Crew 时发生错误: {e}")


def test():
    """
    测试 Crew 执行并返回结果
    """
    inputs = {"project_name": "AI 助手", "current_year": str(datetime.now().year)}

    try:
        MyCrew().crew().test(
            n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"测试 Crew 时发生错误: {e}")


def run_with_trigger():
    """
    使用触发载荷运行 Crew
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("未提供触发载荷，请提供 JSON 格式的载荷参数。")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("提供的触发载荷不是有效的 JSON 格式")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "project_name": "",
        "current_year": "",
    }

    try:
        result = MyCrew().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"使用触发载荷运行 Crew 时发生错误: {e}")
