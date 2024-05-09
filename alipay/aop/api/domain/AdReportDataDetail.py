#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdReportConversionDataDetail import AdReportConversionDataDetail


class AdReportDataDetail(object):

    def __init__(self):
        self._biz_date = None
        self._click = None
        self._conversion_data_list = None
        self._cost = None
        self._creative_name = None
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
        self._scene_name = None

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
    def creative_name(self):
        return self._creative_name

    @creative_name.setter
    def creative_name(self, value):
        self._creative_name = value
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
    def scene_name(self):
        return self._scene_name

    @scene_name.setter
    def scene_name(self, value):
        self._scene_name = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.creative_name:
            if hasattr(self.creative_name, 'to_alipay_dict'):
                params['creative_name'] = self.creative_name.to_alipay_dict()
            else:
                params['creative_name'] = self.creative_name
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
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'click' in d:
            o.click = d['click']
        if 'conversion_data_list' in d:
            o.conversion_data_list = d['conversion_data_list']
        if 'cost' in d:
            o.cost = d['cost']
        if 'creative_name' in d:
            o.creative_name = d['creative_name']
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
        if 'scene_name' in d:
            o.scene_name = d['scene_name']
        return o


