"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class ExchangeReplayService(BaseModuleService):
    MODULE = "exchange_replay"
    ENTITY = "重放任务"
    OPERATION_TERM = "归档"
    LIST_FIELDS = ["重放编号", "归档编号", "重放范围", "起始批次", "截止批次", "重放速率", "覆盖方式", "重放结果"]
    REQUIRED_FIELDS = ["重放编号", "归档编号", "重放范围"]
    STATUS_ORDER = ["草稿", "待重放", "重放中", "已完成", "已取消"]
    ACTION_RULES = {"启动重放": "重放中", "标记完成": "已完成", "取消重放": "已取消"}
    NEGATIVE_ACTIONS = []
