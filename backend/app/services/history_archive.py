"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class HistoryArchiveService(BaseModuleService):
    MODULE = "history_archive"
    ENTITY = "归档卷"
    OPERATION_TERM = "校验"
    LIST_FIELDS = ["归档编号", "批次范围", "归档路径", "卷内条数", "压缩方式", "归档校验值", "驻留策略", "归档水位"]
    REQUIRED_FIELDS = ["归档编号", "批次范围", "归档路径"]
    STATUS_ORDER = ["草稿", "待归档", "已归档", "已销毁"]
    ACTION_RULES = {"启动归档": "待归档", "确认归档": "已归档", "执行销毁": "已销毁"}
    NEGATIVE_ACTIONS = []
