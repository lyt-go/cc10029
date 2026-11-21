"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class TransferLineageService(BaseModuleService):
    MODULE = "transfer_lineage"
    ENTITY = "血缘链路"
    OPERATION_TERM = "采集"
    LIST_FIELDS = ["链路编号", "源端编号", "抽取窗口", "传输批次", "目标编号", "字段契约", "血缘版本", "采集时间"]
    REQUIRED_FIELDS = ["链路编号", "源端编号", "抽取窗口"]
    STATUS_ORDER = ["草稿", "待校验", "已生效", "已停用"]
    ACTION_RULES = {"提交校验": "待校验", "确认生效": "已生效", "标记停用": "已停用"}
    NEGATIVE_ACTIONS = []
