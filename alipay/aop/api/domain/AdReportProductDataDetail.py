#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdReportConversionDataDetail import AdReportConversionDataDetail


class AdReportProductDataDetail(object):

    def __init__(self):
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
        self._creative_id = None
        self._creative_name = None
        self._cvr = None
        self._entity_library_id = None
        self._entity_name = None
        self._entity_no = None
        self._entity_out_id = None
        self._group_id = None
        self._group_name = None
        self._impression = None
        self._market_target_name = None
        self._plan_id = None
        self._plan_name = None
        self._principal_alipay_account = None
        self._principal_id = None
        self._principal_name = None
        self._principal_pid = None

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
    def creative_id(self):
        return self._creative_id

    @creative_id.setter
    def creative_id(self, value):
        self._creative_id = value
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
    def entity_library_id(self):
        return self._entity_library_id

    @entity_library_id.setter
    def entity_library_id(self, value):
        self._entity_library_id = value
    @property
    def entity_name(self):
        return self._entity_name

    @entity_name.setter
    def entity_name(self, value):
        self._entity_name = value
    @property
    def entity_no(self):
        return self._entity_no

    @entity_no.setter
    def entity_no(self, value):
        self._entity_no = value
    @property
    def entity_out_id(self):
        return self._entity_out_id

    @entity_out_id.setter
    def entity_out_id(self, value):
        self._entity_out_id = value
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
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
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


    def to_alipay_dict(self):
        params = dict()
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
        if self.creative_id:
            if hasattr(self.creative_id, 'to_alipay_dict'):
                params['creative_id'] = self.creative_id.to_alipay_dict()
            else:
                params['creative_id'] = self.creative_id
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
        if self.entity_library_id:
            if hasattr(self.entity_library_id, 'to_alipay_dict'):
                params['entity_library_id'] = self.entity_library_id.to_alipay_dict()
            else:
                params['entity_library_id'] = self.entity_library_id
        if self.entity_name:
            if hasattr(self.entity_name, 'to_alipay_dict'):
                params['entity_name'] = self.entity_name.to_alipay_dict()
            else:
                params['entity_name'] = self.entity_name
        if self.entity_no:
            if hasattr(self.entity_no, 'to_alipay_dict'):
                params['entity_no'] = self.entity_no.to_alipay_dict()
            else:
                params['entity_no'] = self.entity_no
        if self.entity_out_id:
            if hasattr(self.entity_out_id, 'to_alipay_dict'):
                params['entity_out_id'] = self.entity_out_id.to_alipay_dict()
            else:
                params['entity_out_id'] = self.entity_out_id
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
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdReportProductDataDetail()
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
        if 'creative_id' in d:
            o.creative_id = d['creative_id']
        if 'creative_name' in d:
            o.creative_name = d['creative_name']
        if 'cvr' in d:
            o.cvr = d['cvr']
        if 'entity_library_id' in d:
            o.entity_library_id = d['entity_library_id']
        if 'entity_name' in d:
            o.entity_name = d['entity_name']
        if 'entity_no' in d:
            o.entity_no = d['entity_no']
        if 'entity_out_id' in d:
            o.entity_out_id = d['entity_out_id']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'impression' in d:
            o.impression = d['impression']
        if 'market_target_name' in d:
            o.market_target_name = d['market_target_name']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'plan_name' in d:
            o.plan_name = d['plan_name']
        if 'principal_alipay_account' in d:
            o.principal_alipay_account = d['principal_alipay_account']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'principal_name' in d:
            o.principal_name = d['principal_name']
        if 'principal_pid' in d:
            o.principal_pid = d['principal_pid']
        return o


