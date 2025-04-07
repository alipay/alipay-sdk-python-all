#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdReportConversionDataDetail import AdReportConversionDataDetail


class AdReportDataDetail(object):

    def __init__(self):
        self._agent_alipay_account = None
        self._agent_name = None
        self._avg_conv_cost = None
        self._biz_date = None
        self._click = None
        self._click_rate = None
        self._conv_result = None
        self._conversion_data_list = None
        self._cost = None
        self._cost_format = None
        self._cpc = None
        self._cpm = None
        self._creative_name = None
        self._cvr = None
        self._data_id = None
        self._group_id = None
        self._group_name = None
        self._impression = None
        self._market_target_name = None
        self._order_id = None
        self._order_name = None
        self._plan_id = None
        self._plan_name = None
        self._principal_alipay_account = None
        self._principal_name = None
        self._principal_pid = None
        self._scene_name = None

    @property
    def agent_alipay_account(self):
        return self._agent_alipay_account

    @agent_alipay_account.setter
    def agent_alipay_account(self, value):
        self._agent_alipay_account = value
    @property
    def agent_name(self):
        return self._agent_name

    @agent_name.setter
    def agent_name(self, value):
        self._agent_name = value
    @property
    def avg_conv_cost(self):
        return self._avg_conv_cost

    @avg_conv_cost.setter
    def avg_conv_cost(self, value):
        self._avg_conv_cost = value
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def click(self):
        return self._click

    @click.setter
    def click(self, value):
        self._click = value
    @property
    def click_rate(self):
        return self._click_rate

    @click_rate.setter
    def click_rate(self, value):
        self._click_rate = value
    @property
    def conv_result(self):
        return self._conv_result

    @conv_result.setter
    def conv_result(self, value):
        self._conv_result = value
    @property
    def conversion_data_list(self):
        return self._conversion_data_list

    @conversion_data_list.setter
    def conversion_data_list(self, value):
        if isinstance(value, list):
            self._conversion_data_list = list()
            for i in value:
                if isinstance(i, AdReportConversionDataDetail):
                    self._conversion_data_list.append(i)
                else:
                    self._conversion_data_list.append(AdReportConversionDataDetail.from_alipay_dict(i))
    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value
    @property
    def cost_format(self):
        return self._cost_format

    @cost_format.setter
    def cost_format(self, value):
        self._cost_format = value
    @property
    def cpc(self):
        return self._cpc

    @cpc.setter
    def cpc(self, value):
        self._cpc = value
    @property
    def cpm(self):
        return self._cpm

    @cpm.setter
    def cpm(self, value):
        self._cpm = value
    @property
    def creative_name(self):
        return self._creative_name

    @creative_name.setter
    def creative_name(self, value):
        self._creative_name = value
    @property
    def cvr(self):
        return self._cvr

    @cvr.setter
    def cvr(self, value):
        self._cvr = value
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def impression(self):
        return self._impression

    @impression.setter
    def impression(self, value):
        self._impression = value
    @property
    def market_target_name(self):
        return self._market_target_name

    @market_target_name.setter
    def market_target_name(self, value):
        self._market_target_name = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_name(self):
        return self._order_name

    @order_name.setter
    def order_name(self, value):
        self._order_name = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def principal_alipay_account(self):
        return self._principal_alipay_account

    @principal_alipay_account.setter
    def principal_alipay_account(self, value):
        self._principal_alipay_account = value
    @property
    def principal_name(self):
        return self._principal_name

    @principal_name.setter
    def principal_name(self, value):
        self._principal_name = value
    @property
    def principal_pid(self):
        return self._principal_pid

    @principal_pid.setter
    def principal_pid(self, value):
        self._principal_pid = value
    @property
    def scene_name(self):
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value):
        self._scene_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_alipay_account:
            if hasattr(self.agent_alipay_account, 'to_alipay_dict'):
                params['agent_alipay_account'] = self.agent_alipay_account.to_alipay_dict()
            else:
                params['agent_alipay_account'] = self.agent_alipay_account
        if self.agent_name:
            if hasattr(self.agent_name, 'to_alipay_dict'):
                params['agent_name'] = self.agent_name.to_alipay_dict()
            else:
                params['agent_name'] = self.agent_name
        if self.avg_conv_cost:
            if hasattr(self.avg_conv_cost, 'to_alipay_dict'):
                params['avg_conv_cost'] = self.avg_conv_cost.to_alipay_dict()
            else:
                params['avg_conv_cost'] = self.avg_conv_cost
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.click:
            if hasattr(self.click, 'to_alipay_dict'):
                params['click'] = self.click.to_alipay_dict()
            else:
                params['click'] = self.click
        if self.click_rate:
            if hasattr(self.click_rate, 'to_alipay_dict'):
                params['click_rate'] = self.click_rate.to_alipay_dict()
            else:
                params['click_rate'] = self.click_rate
        if self.conv_result:
            if hasattr(self.conv_result, 'to_alipay_dict'):
                params['conv_result'] = self.conv_result.to_alipay_dict()
            else:
                params['conv_result'] = self.conv_result
        if self.conversion_data_list:
            if isinstance(self.conversion_data_list, list):
                for i in range(0, len(self.conversion_data_list)):
                    element = self.conversion_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.conversion_data_list[i] = element.to_alipay_dict()
            if hasattr(self.conversion_data_list, 'to_alipay_dict'):
                params['conversion_data_list'] = self.conversion_data_list.to_alipay_dict()
            else:
                params['conversion_data_list'] = self.conversion_data_list
        if self.cost:
            if hasattr(self.cost, 'to_alipay_dict'):
                params['cost'] = self.cost.to_alipay_dict()
            else:
                params['cost'] = self.cost
        if self.cost_format:
            if hasattr(self.cost_format, 'to_alipay_dict'):
                params['cost_format'] = self.cost_format.to_alipay_dict()
            else:
                params['cost_format'] = self.cost_format
        if self.cpc:
            if hasattr(self.cpc, 'to_alipay_dict'):
                params['cpc'] = self.cpc.to_alipay_dict()
            else:
                params['cpc'] = self.cpc
        if self.cpm:
            if hasattr(self.cpm, 'to_alipay_dict'):
                params['cpm'] = self.cpm.to_alipay_dict()
            else:
                params['cpm'] = self.cpm
        if self.creative_name:
            if hasattr(self.creative_name, 'to_alipay_dict'):
                params['creative_name'] = self.creative_name.to_alipay_dict()
            else:
                params['creative_name'] = self.creative_name
        if self.cvr:
            if hasattr(self.cvr, 'to_alipay_dict'):
                params['cvr'] = self.cvr.to_alipay_dict()
            else:
                params['cvr'] = self.cvr
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.impression:
            if hasattr(self.impression, 'to_alipay_dict'):
                params['impression'] = self.impression.to_alipay_dict()
            else:
                params['impression'] = self.impression
        if self.market_target_name:
            if hasattr(self.market_target_name, 'to_alipay_dict'):
                params['market_target_name'] = self.market_target_name.to_alipay_dict()
            else:
                params['market_target_name'] = self.market_target_name
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_name:
            if hasattr(self.order_name, 'to_alipay_dict'):
                params['order_name'] = self.order_name.to_alipay_dict()
            else:
                params['order_name'] = self.order_name
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.plan_name:
            if hasattr(self.plan_name, 'to_alipay_dict'):
                params['plan_name'] = self.plan_name.to_alipay_dict()
            else:
                params['plan_name'] = self.plan_name
        if self.principal_alipay_account:
            if hasattr(self.principal_alipay_account, 'to_alipay_dict'):
                params['principal_alipay_account'] = self.principal_alipay_account.to_alipay_dict()
            else:
                params['principal_alipay_account'] = self.principal_alipay_account
        if self.principal_name:
            if hasattr(self.principal_name, 'to_alipay_dict'):
                params['principal_name'] = self.principal_name.to_alipay_dict()
            else:
                params['principal_name'] = self.principal_name
        if self.principal_pid:
            if hasattr(self.principal_pid, 'to_alipay_dict'):
                params['principal_pid'] = self.principal_pid.to_alipay_dict()
            else:
                params['principal_pid'] = self.principal_pid
        if self.scene_name:
            if hasattr(self.scene_name, 'to_alipay_dict'):
                params['scene_name'] = self.scene_name.to_alipay_dict()
            else:
                params['scene_name'] = self.scene_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdReportDataDetail()
        if 'agent_alipay_account' in d:
            o.agent_alipay_account = d['agent_alipay_account']
        if 'agent_name' in d:
            o.agent_name = d['agent_name']
        if 'avg_conv_cost' in d:
            o.avg_conv_cost = d['avg_conv_cost']
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'click' in d:
            o.click = d['click']
        if 'click_rate' in d:
            o.click_rate = d['click_rate']
        if 'conv_result' in d:
            o.conv_result = d['conv_result']
        if 'conversion_data_list' in d:
            o.conversion_data_list = d['conversion_data_list']
        if 'cost' in d:
            o.cost = d['cost']
        if 'cost_format' in d:
            o.cost_format = d['cost_format']
        if 'cpc' in d:
            o.cpc = d['cpc']
        if 'cpm' in d:
            o.cpm = d['cpm']
        if 'creative_name' in d:
            o.creative_name = d['creative_name']
        if 'cvr' in d:
            o.cvr = d['cvr']
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'impression' in d:
            o.impression = d['impression']
        if 'market_target_name' in d:
            o.market_target_name = d['market_target_name']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_name' in d:
            o.order_name = d['order_name']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'principal_alipay_account' in d:
            o.principal_alipay_account = d['principal_alipay_account']
        if 'principal_name' in d:
            o.principal_name = d['principal_name']
        if 'principal_pid' in d:
            o.principal_pid = d['principal_pid']
        if 'scene_name' in d:
            o.scene_name = d['scene_name']
        return o


