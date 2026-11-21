"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class ExtractWindowService(BaseModuleService):
    MODULE = "extract_window"
    ENTITY = "抽取窗口"
    OPERATION_TERM = "切分"
    LIST_FIELDS = ["窗口编号", "源端编号", "增量字段", "窗口起点", "窗口终点", "抽取条数", "窗口类型", "推进水位"]
    REQUIRED_FIELDS = ["窗口编号", "源端编号", "增量字段"]
    STATUS_ORDER = ["草稿", "待抽取", "抽取中", "已闭合"]
    ACTION_RULES = {"启动抽取": "抽取中", "闭合窗口": "已闭合", "标记作废": "已闭合"}
    NEGATIVE_ACTIONS = []
