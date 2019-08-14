#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO
from alipay.aop.api.domain.CreditPayRefuseVO import CreditPayRefuseVO
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO


class CreditPayAssetBaseVO(object):

    def __init__(self):
        self._available_amt = None
        self._credit_enough = None
        self._enable = None
        self._name = None
        self._pre_repay_desc = None
        self._refuse_info = None
        self._repay_day_desc = None
        self._scheme_date = None
        self._scheme_id = None
        self._total_amt = None
        self._type = None

    @property
    def available_amt(self):
        return self._available_amt

    @available_amt.setter
    def available_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._available_amt = value
        else:
            self._available_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def credit_enough(self):
        return self._credit_enough

    @credit_enough.setter
    def credit_enough(self, value):
        self._credit_enough = value
    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def pre_repay_desc(self):
        return self._pre_repay_desc

    @pre_repay_desc.setter
    def pre_repay_desc(self, value):
        self._pre_repay_desc = value
    @property
    def refuse_info(self):
        return self._refuse_info

    @refuse_info.setter
    def refuse_info(self, value):
        if isinstance(value, CreditPayRefuseVO):
            self._refuse_info = value
        else:
            self._refuse_info = CreditPayRefuseVO.from_alipay_dict(value)
    @property
    def repay_day_desc(self):
        return self._repay_day_desc

    @repay_day_desc.setter
    def repay_day_desc(self, value):
        self._repay_day_desc = value
    @property
    def scheme_date(self):
        return self._scheme_date

    @scheme_date.setter
    def scheme_date(self, value):
        self._scheme_date = value
    @property
    def scheme_id(self):
        return self._scheme_id

    @scheme_id.setter
    def scheme_id(self, value):
        self._scheme_id = value
    @property
    def total_amt(self):
        return self._total_amt

    @total_amt.setter
    def total_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._total_amt = value
        else:
            self._total_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_amt:
            if hasattr(self.available_amt, 'to_alipay_dict'):
                params['available_amt'] = self.available_amt.to_alipay_dict()
            else:
                params['available_amt'] = self.available_amt
        if self.credit_enough:
            if hasattr(self.credit_enough, 'to_alipay_dict'):
                params['credit_enough'] = self.credit_enough.to_alipay_dict()
            else:
                params['credit_enough'] = self.credit_enough
        if self.enable:
            if hasattr(self.enable, 'to_alipay_dict'):
                params['enable'] = self.enable.to_alipay_dict()
            else:
                params['enable'] = self.enable
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.pre_repay_desc:
            if hasattr(self.pre_repay_desc, 'to_alipay_dict'):
                params['pre_repay_desc'] = self.pre_repay_desc.to_alipay_dict()
            else:
                params['pre_repay_desc'] = self.pre_repay_desc
        if self.refuse_info:
            if hasattr(self.refuse_info, 'to_alipay_dict'):
                params['refuse_info'] = self.refuse_info.to_alipay_dict()
            else:
                params['refuse_info'] = self.refuse_info
        if self.repay_day_desc:
            if hasattr(self.repay_day_desc, 'to_alipay_dict'):
                params['repay_day_desc'] = self.repay_day_desc.to_alipay_dict()
            else:
                params['repay_day_desc'] = self.repay_day_desc
        if self.scheme_date:
            if hasattr(self.scheme_date, 'to_alipay_dict'):
                params['scheme_date'] = self.scheme_date.to_alipay_dict()
            else:
                params['scheme_date'] = self.scheme_date
        if self.scheme_id:
            if hasattr(self.scheme_id, 'to_alipay_dict'):
                params['scheme_id'] = self.scheme_id.to_alipay_dict()
            else:
                params['scheme_id'] = self.scheme_id
        if self.total_amt:
            if hasattr(self.total_amt, 'to_alipay_dict'):
                params['total_amt'] = self.total_amt.to_alipay_dict()
            else:
                params['total_amt'] = self.total_amt
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
        o = CreditPayAssetBaseVO()
        if 'available_amt' in d:
            o.available_amt = d['available_amt']
        if 'credit_enough' in d:
            o.credit_enough = d['credit_enough']
        if 'enable' in d:
            o.enable = d['enable']
        if 'name' in d:
            o.name = d['name']
        if 'pre_repay_desc' in d:
            o.pre_repay_desc = d['pre_repay_desc']
        if 'refuse_info' in d:
            o.refuse_info = d['refuse_info']
        if 'repay_day_desc' in d:
            o.repay_day_desc = d['repay_day_desc']
        if 'scheme_date' in d:
            o.scheme_date = d['scheme_date']
        if 'scheme_id' in d:
            o.scheme_id = d['scheme_id']
        if 'total_amt' in d:
            o.total_amt = d['total_amt']
        if 'type' in d:
            o.type = d['type']
        return o


