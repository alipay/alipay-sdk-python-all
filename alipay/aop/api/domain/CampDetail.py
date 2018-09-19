#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityOrderDTO import ActivityOrderDTO
from alipay.aop.api.domain.BudgetInfo import BudgetInfo
from alipay.aop.api.domain.ConstraintInfo import ConstraintInfo
from alipay.aop.api.domain.PromoTool import PromoTool
from alipay.aop.api.domain.PublishChannel import PublishChannel
from alipay.aop.api.domain.RecruitInfo import RecruitInfo


class CampDetail(object):

    def __init__(self):
        self._activity_orders = None
        self._audit_status = None
        self._auto_delay_flag = None
        self._budget_info = None
        self._constraint_info = None
        self._desc = None
        self._end_time = None
        self._ext_info = None
        self._id = None
        self._name = None
        self._promo_tools = None
        self._publish_channels = None
        self._recruit_info = None
        self._start_time = None
        self._status = None
        self._type = None

    @property
    def activity_orders(self):
        return self._activity_orders

    @activity_orders.setter
    def activity_orders(self, value):
        if isinstance(value, list):
            self._activity_orders = list()
            for i in value:
                if isinstance(i, ActivityOrderDTO):
                    self._activity_orders.append(i)
                else:
                    self._activity_orders.append(ActivityOrderDTO.from_alipay_dict(i))
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def auto_delay_flag(self):
        return self._auto_delay_flag

    @auto_delay_flag.setter
    def auto_delay_flag(self, value):
        self._auto_delay_flag = value
    @property
    def budget_info(self):
        return self._budget_info

    @budget_info.setter
    def budget_info(self, value):
        if isinstance(value, BudgetInfo):
            self._budget_info = value
        else:
            self._budget_info = BudgetInfo.from_alipay_dict(value)
    @property
    def constraint_info(self):
        return self._constraint_info

    @constraint_info.setter
    def constraint_info(self, value):
        if isinstance(value, ConstraintInfo):
            self._constraint_info = value
        else:
            self._constraint_info = ConstraintInfo.from_alipay_dict(value)
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def promo_tools(self):
        return self._promo_tools

    @promo_tools.setter
    def promo_tools(self, value):
        if isinstance(value, list):
            self._promo_tools = list()
            for i in value:
                if isinstance(i, PromoTool):
                    self._promo_tools.append(i)
                else:
                    self._promo_tools.append(PromoTool.from_alipay_dict(i))
    @property
    def publish_channels(self):
        return self._publish_channels

    @publish_channels.setter
    def publish_channels(self, value):
        if isinstance(value, list):
            self._publish_channels = list()
            for i in value:
                if isinstance(i, PublishChannel):
                    self._publish_channels.append(i)
                else:
                    self._publish_channels.append(PublishChannel.from_alipay_dict(i))
    @property
    def recruit_info(self):
        return self._recruit_info

    @recruit_info.setter
    def recruit_info(self, value):
        if isinstance(value, RecruitInfo):
            self._recruit_info = value
        else:
            self._recruit_info = RecruitInfo.from_alipay_dict(value)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_orders:
            if isinstance(self.activity_orders, list):
                for i in range(0, len(self.activity_orders)):
                    element = self.activity_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_orders[i] = element.to_alipay_dict()
            if hasattr(self.activity_orders, 'to_alipay_dict'):
                params['activity_orders'] = self.activity_orders.to_alipay_dict()
            else:
                params['activity_orders'] = self.activity_orders
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.auto_delay_flag:
            if hasattr(self.auto_delay_flag, 'to_alipay_dict'):
                params['auto_delay_flag'] = self.auto_delay_flag.to_alipay_dict()
            else:
                params['auto_delay_flag'] = self.auto_delay_flag
        if self.budget_info:
            if hasattr(self.budget_info, 'to_alipay_dict'):
                params['budget_info'] = self.budget_info.to_alipay_dict()
            else:
                params['budget_info'] = self.budget_info
        if self.constraint_info:
            if hasattr(self.constraint_info, 'to_alipay_dict'):
                params['constraint_info'] = self.constraint_info.to_alipay_dict()
            else:
                params['constraint_info'] = self.constraint_info
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.promo_tools:
            if isinstance(self.promo_tools, list):
                for i in range(0, len(self.promo_tools)):
                    element = self.promo_tools[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_tools[i] = element.to_alipay_dict()
            if hasattr(self.promo_tools, 'to_alipay_dict'):
                params['promo_tools'] = self.promo_tools.to_alipay_dict()
            else:
                params['promo_tools'] = self.promo_tools
        if self.publish_channels:
            if isinstance(self.publish_channels, list):
                for i in range(0, len(self.publish_channels)):
                    element = self.publish_channels[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.publish_channels[i] = element.to_alipay_dict()
            if hasattr(self.publish_channels, 'to_alipay_dict'):
                params['publish_channels'] = self.publish_channels.to_alipay_dict()
            else:
                params['publish_channels'] = self.publish_channels
        if self.recruit_info:
            if hasattr(self.recruit_info, 'to_alipay_dict'):
                params['recruit_info'] = self.recruit_info.to_alipay_dict()
            else:
                params['recruit_info'] = self.recruit_info
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CampDetail()
        if 'activity_orders' in d:
            o.activity_orders = d['activity_orders']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'auto_delay_flag' in d:
            o.auto_delay_flag = d['auto_delay_flag']
        if 'budget_info' in d:
            o.budget_info = d['budget_info']
        if 'constraint_info' in d:
            o.constraint_info = d['constraint_info']
        if 'desc' in d:
            o.desc = d['desc']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'promo_tools' in d:
            o.promo_tools = d['promo_tools']
        if 'publish_channels' in d:
            o.publish_channels = d['publish_channels']
        if 'recruit_info' in d:
            o.recruit_info = d['recruit_info']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        if 'type' in d:
            o.type = d['type']
        return o


