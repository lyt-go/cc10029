"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class ConflictResolveService(BaseModuleService):
    MODULE = "conflict_resolve"
    ENTITY = "冲突记录"
    OPERATION_TERM = "校验"
    LIST_FIELDS = ["冲突编号", "记录主键", "冲突字段", "源端取值", "目标取值", "裁决方式", "裁决依据", "裁决时间"]
    REQUIRED_FIELDS = ["冲突编号", "记录主键", "冲突字段"]
    STATUS_ORDER = ["草稿", "待裁决", "已裁决", "已挂起"]
    ACTION_RULES = {"提交裁决": "待裁决", "确认裁决": "已裁决", "标记挂起": "已挂起"}
    NEGATIVE_ACTIONS = []
