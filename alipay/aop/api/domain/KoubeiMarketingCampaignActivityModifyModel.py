#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BudgetInfo import BudgetInfo
from alipay.aop.api.domain.ConstraintInfo import ConstraintInfo
from alipay.aop.api.domain.PromoTool import PromoTool
from alipay.aop.api.domain.PublishChannel import PublishChannel
from alipay.aop.api.domain.RecruitTool import RecruitTool


class KoubeiMarketingCampaignActivityModifyModel(object):

    def __init__(self):
        self._auto_delay_flag = None
        self._budget_info = None
        self._camp_id = None
        self._constraint_info = None
        self._desc = None
        self._end_time = None
        self._ext_info = None
        self._name = None
        self._operator_id = None
        self._operator_type = None
        self._out_biz_no = None
        self._promo_tools = None
        self._publish_channels = None
        self._recruit_tool = None
        self._start_time = None
        self._type = None

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
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
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
    def recruit_tool(self):
        return self._recruit_tool

    @recruit_tool.setter
    def recruit_tool(self, value):
        if isinstance(value, RecruitTool):
            self._recruit_tool = value
        else:
            self._recruit_tool = RecruitTool.from_alipay_dict(value)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        if self.recruit_tool:
            if hasattr(self.recruit_tool, 'to_alipay_dict'):
                params['recruit_tool'] = self.recruit_tool.to_alipay_dict()
            else:
                params['recruit_tool'] = self.recruit_tool
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
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
        o = KoubeiMarketingCampaignActivityModifyModel()
        if 'auto_delay_flag' in d:
            o.auto_delay_flag = d['auto_delay_flag']
        if 'budget_info' in d:
            o.budget_info = d['budget_info']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'constraint_info' in d:
            o.constraint_info = d['constraint_info']
        if 'desc' in d:
            o.desc = d['desc']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'name' in d:
            o.name = d['name']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'promo_tools' in d:
            o.promo_tools = d['promo_tools']
        if 'publish_channels' in d:
            o.publish_channels = d['publish_channels']
        if 'recruit_tool' in d:
            o.recruit_tool = d['recruit_tool']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'type' in d:
            o.type = d['type']
        return o


