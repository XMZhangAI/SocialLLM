General_Judge_Prompt = """
### 任务介绍
请作为一个公正的裁判者，评估人工智能助手对下面显示的用户问题提供的回答的质量。您的评估应考虑角色记忆的准确性。
给定角色设定、角色和用户（用户可能是另一个角色）间的一段对话上下文、在当前对话上下文下用户提出的一个问题（即 用户问题）、以及角色针对用户问题的回复（即 角色回复），任务目标是**标注角色回复是否与对话上下文中某一轮次或某几轮次角色的回复存在冲突（答案不一致）**，你需要按照下述步骤对可能存在的冲突进行标注。
### 任务流程
1. 依据用户问题，确定正面回答问题应有的内容，并与角色回复进行对比，分析答案内容是否明确，如果没有直接回答，属于答非所问（2分）；如果只回答了部分，依据覆盖程度判断是3分还是4分。
2. 依据标注指导，逐条分析数据对该条要求的符合程度，并输出解释。
3. 在评估所有指导条目后，输出标注结果。
4. 最终结果只以json格式输出，不要输出其他内容。输出示例：{{direct: 答非所问应有的内容，以及是否属于答非所问，给出解释, exp: 对照标注指导的逐条解释，在每一条，首先输出标注的序号，然后对照分析答案是否符合、为什么, label: 标注的分值}}。
### 标注指导：
{guideline}
### 角色设定：
{character_prompt}
### 提示：
“### 上下文”是用户和角色之间的对话，“### 上下文”中角色的回复并不是由模型生成的，而是真实已经存在的，只有“### 模型回复”部分的内容是由模型模仿角色生成的回复。
### 上下文:
{context}
### 模型回复:
{response}
"""

General_Judge_Prompt = \
"""请你扮演一个公正的裁判，根据下面的任务要求完成任务。

[任务要求]
{task_guideline}

注意：
(1) 请依据任务要求对角色回复进行评分，同时给出客观的评分依据。
(2) 输出json格式，示例：{{"explanation": 评分依据, "score": 分值}}。

[角色设定]
{character_profile}

[多轮对话]
{dialogue}

[用户发言]
{user_query}

[角色回复]
{character_response}
"""

# Memory_Guideline = \
# """给定角色设定、角色和另一个角色的多轮对话、用户发言和角色回复，你的任务目标是评估给定的角色回复是否与多轮对话中的历史角色回复在内容上保持一致。你需要按照下面的打分标准对角色回复进行打分：

# (1) 1分：角色回复与多轮对话中的历史角色回复在与用户发言相关的内容上存在不一致。
# (2) 2分：角色回复与多轮对话中的历史角色回复在与用户发言相关的内容上不存在不一致，但角色回复没有回答用户发言的问题，并且在逻辑上不连贯。
# (3) 3分：角色回复与多轮对话中的历史角色回复在与用户发言相关的内容上不存在不一致，但角色回复没有回答用户发言的问题，但是在逻辑上连贯。
# (4) 4分：角色回复与多轮对话中的历史角色回复在与用户发言相关的内容上不存在不一致，角色回复回答了用户发言的问题，但角色回复仅包含多轮对话中的历史角色回复中的部分答案。
# (5) 5分：角色回复与多轮对话中的历史角色回复在与用户发言相关的内容上不存在不一致，角色回复回答了用户发言的问题，并且角色回复包含了多轮对话中的历史角色回复中的全部答案。"""

# EVALUATION_GUIDELINE = {
#     "memory": Memory_Guideline,
# }

# Memory_Guideline_Refine = \
# """给定角色设定、角色和另一个角色的多轮对话、用户发言和角色回复，你的任务目标是评估给定的角色回复是否与多轮对话中某一轮次或某几轮次的角色表述的答案存在不一致，不一致需要从语义或内容上进行判断。打分标准如下：

# (1) 1分：角色回复与多轮对话中的答案存在不一致。
# (2) 2分：角色回复没有回答用户发言的问题，并且在逻辑上不连贯。
# (3) 3分：角色回复回答了用户发言的问题，但是角色回复没有包含任何多轮对话中给出的答案。
# (4) 4分：角色回复回答了用户发言的问题，但是角色回复仅包含多轮对话中给出的部分答案。
# (5) 5分：角色回复回答了用户发言的问题，并且角色回复包含了多轮对话中给出的全部答案。"""

Memory_Guideline_Refine_refine = \
"""给定角色设定、角色和另一个角色的多轮对话、用户发言和角色回复，你的任务目标是评估给定的角色回复是否与多轮对话中某一轮次或某几轮次的角色表述的答案存在不一致，不一致需要从语义或内容上进行判断。打分标准如下：

(1) 1分：角色回复与多轮对话中的答案存在不一致。
(2) 2分：角色回复没有回答用户发言的问题，并且在逻辑上不连贯。
(3) 3分：角色回复没有回答用户发言的问题，但是在逻辑上连贯。
(4) 4分：角色回复与多轮对话中的答案不存在不一致，但是角色回复仅覆盖包含多轮对话中给出的部分答案。
(5) 5分：角色回复与多轮对话中的答案不存在不一致，并且角色回复覆盖了多轮对话中给出的全部答案。"""

# Memory_Guideline_Refine_refine_refine = \
# """给定{character_name}的角色设定、角色和另一个角色的多轮对话、用户发言和{character_name}的角色回复，你的任务目标是评估给定的{character_name}的角色回复是否与多轮对话中某一轮次或某几轮次的{character_name}表述的答案存在不一致，不一致需要从语义或内容上进行判断。打分标准如下：

# (1) 1分：{character_name}的角色回复与多轮对话中的答案存在不一致。
# (2) 2分：{character_name}的角色回复没有回答用户发言的问题，并且在逻辑上不连贯。
# (3) 3分：{character_name}的角色回复没有回答用户发言的问题，但是在逻辑上连贯。
# (4) 4分：{character_name}的角色回复与多轮对话中的答案不存在不一致，但是角色回复仅覆盖多轮对话中{character_name}表述的部分答案。
# (5) 5分：{character_name}的角色回复与多轮对话中的答案不存在不一致，并且角色回复覆盖了多轮对话中{character_name}表述的所有答案。"""

# Memory_Guideline_Refine_refine = \
# """给定角色设定、角色和另一个角色的多轮对话、用户发言和角色回复，你的任务目标是评估给定的角色回复是否与多轮对话中某一轮次或某几轮次的角色表述的答案存在不一致，不一致需要从语义或内容上进行判断。请依次按照如下打分标准进行评估：

# (1) 1分：角色回复与多轮对话中的答案存在不一致。
# (2) 2分：角色回复没有回答用户发言的问题，并且在逻辑上不连贯。
# (3) 3分：角色回复没有回答用户发言的问题，但是在逻辑上连贯。
# (4) 4分：角色回复与多轮对话中的答案不存在不一致，但是角色回复仅覆盖多轮对话中角色表述的部分答案。
# (5) 5分：角色回复与多轮对话中的答案不存在不一致，并且角色回复覆盖了多轮对话中角色表述的所有答案。"""

Fact_Acc_Guideline = \
"""给定角色设定、角色和另一个角色的多轮对话、用户发言和相应的角色回复，你的任务目标是以角色设定作为参考答案，评估给定的角色回复是否正确地回答了用户发言，即角色回复是否与角色设定中的答案在语义或内容保持一致，角色回复中的答案未在角色设定中出现时，不作为评判不一致的依据。打分标准如下：

(1) 1分：角色回复与角色设定中的答案不匹配，即角色回复错误地回复了用户发言的问题。
(2) 2分：角色回复没有回答用户发言的问题，即答非所问，角色回复与用户发言在逻辑上在逻辑上表现的不自然和不流畅。
(3) 3分：角色回复没有回答用户发言的问题，但角色回复与用户发言在逻辑上表现的自然和流畅。
(4) 4分：角色回复仅覆盖包含角色设定中给出的部分答案，并且角色回复与角色设定中的答案不存在不一致。
(5) 5分：角色回复覆盖了角色设定中给出的全部答案，并且角色回复与角色设定中的答案不存在不一致。"""


Fact_Acc_Guideline_gpt_refine = \
"""在此标注任务中，您将根据角色设定、用户发言和角色回复来评估角色回复是否正确地回应了用户发言。角色回复的正确性是基于是否与角色设定中提供的信息在语义和内容上保持一致。具体评分标准如下：

(1) 1分：角色回复与角色设定中提供的答案不一致，明显偏离角色设定提供的答案，或提供了完全错误的答案。
(2) 2分：角色回复没有回答用户发言的问题，即答非所问，角色回复与用户发言在逻辑上表现的不自然和不流畅。
(3) 3分：角色回复未完全回答或没有回答用户发言的问题，但角色回复与用户发言在逻辑上是自然且流畅的，展示了适当的对话上下文的理解。
(4) 4分：角色回复正确地覆盖了角色设定中提到的部分信息，但未完全覆盖所有相关信息。
(5) 5分：角色回复全面且准确地覆盖了角色设定中的全部信息，完美回应了用户的发言。"""

# 2分：角色回复未能直接回答用户发言，与用户发言不相关（比如，话题），从语义或逻辑上与用户的发言不匹配，显示出明显的不自然或不流畅。
# 3分：角色回复虽未完全回答或直接回答用户的问题，但其回答在逻辑上与用户发言自然且流畅，展示了适当的上下文理解。

EVALUATION_GUIDELINE = {
    "memory": Memory_Guideline_Refine_refine,
    "fact_acc": Fact_Acc_Guideline_gpt_refine
}
