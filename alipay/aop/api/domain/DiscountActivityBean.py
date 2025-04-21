#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MarketingParamBean import MarketingParamBean


class DiscountActivityBean(object):

    def __init__(self):
        self._activity_desc = None
        self._activity_detail_id = None
        self._activity_id = None
        self._activity_name = None
        self._activity_type = None
        self._marketing_param = None
        self._participate_id = None
        self._participate_type = None
        self._shop_id = None
        self._status = None

    @property
    def activity_desc(self):
        return self._activity_desc

    @activity_desc.setter
    def activity_desc(self, value):
        self._activity_desc = value
    @property
    def activity_detail_id(self):
        return self._activity_detail_id

    @activity_detail_id.setter
    def activity_detail_id(self, value):
        self._activity_detail_id = value
    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def marketing_param(self):
        return self._marketing_param

    @marketing_param.setter
    def marketing_param(self, value):
        if isinstance(value, MarketingParamBean):
            self._marketing_param = value
        else:
            self._marketing_param = MarketingParamBean.from_alipay_dict(value)
    @property
    def participate_id(self):
        return self._participate_id

    @participate_id.setter
    def participate_id(self, value):
        self._participate_id = value
    @property
    def participate_type(self):
        return self._participate_type

    @participate_type.setter
    def participate_type(self, value):
        self._participate_type = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_desc:
            if hasattr(self.activity_desc, 'to_alipay_dict'):
                params['activity_desc'] = self.activity_desc.to_alipay_dict()
            else:
                params['activity_desc'] = self.activity_desc
        if self.activity_detail_id:
            if hasattr(self.activity_detail_id, 'to_alipay_dict'):
                params['activity_detail_id'] = self.activity_detail_id.to_alipay_dict()
            else:
                params['activity_detail_id'] = self.activity_detail_id
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.marketing_param:
            if hasattr(self.marketing_param, 'to_alipay_dict'):
                params['marketing_param'] = self.marketing_param.to_alipay_dict()
            else:
                params['marketing_param'] = self.marketing_param
        if self.participate_id:
            if hasattr(self.participate_id, 'to_alipay_dict'):
                params['participate_id'] = self.participate_id.to_alipay_dict()
            else:
                params['participate_id'] = self.participate_id
        if self.participate_type:
            if hasattr(self.participate_type, 'to_alipay_dict'):
                params['participate_type'] = self.participate_type.to_alipay_dict()
            else:
                params['participate_type'] = self.participate_type
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiscountActivityBean()
        if 'activity_desc' in d:
            o.activity_desc = d['activity_desc']
        if 'activity_detail_id' in d:
            o.activity_detail_id = d['activity_detail_id']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'marketing_param' in d:
            o.marketing_param = d['marketing_param']
        if 'participate_id' in d:
            o.participate_id = d['participate_id']
        if 'participate_type' in d:
            o.participate_type = d['participate_type']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        return o


