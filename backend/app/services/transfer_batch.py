"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class TransferBatchService(BaseModuleService):
    MODULE = "transfer_batch"
    ENTITY = "传输批次"
    OPERATION_TERM = "水位"
    LIST_FIELDS = ["批次编号", "窗口编号", "目标编号", "记录条数", "字节总量", "分片大小", "传输状态", "批次水位"]
    REQUIRED_FIELDS = ["批次编号", "窗口编号", "目标编号"]
    STATUS_ORDER = ["草稿", "待传输", "传输中", "已完成", "已失败"]
    ACTION_RULES = {"启动传输": "传输中", "标记完成": "已完成", "标记失败": "已失败"}
    NEGATIVE_ACTIONS = []
