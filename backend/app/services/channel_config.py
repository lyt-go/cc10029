"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class ChannelConfigService(BaseModuleService):
    MODULE = "channel_config"
    ENTITY = "传输通道"
    OPERATION_TERM = "校验"
    LIST_FIELDS = ["通道编号", "传输协议", "并发连接数", "重试间隔", "超时秒数", "加密方式", "通道类型", "配置版本"]
    REQUIRED_FIELDS = ["通道编号", "传输协议", "并发连接数"]
    STATUS_ORDER = ["草稿", "待校验", "已生效", "已停用"]
    ACTION_RULES = {"提交校验": "待校验", "确认生效": "已生效", "标记停用": "已停用"}
    NEGATIVE_ACTIONS = []
