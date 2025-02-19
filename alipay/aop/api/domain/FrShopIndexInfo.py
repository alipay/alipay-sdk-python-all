#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FrShopIndexInfo(object):

    def __init__(self):
        self._month = None
        self._sales_amount_12_m = None
        self._sales_amount_1_m = None
        self._sales_amount_3_m = None
        self._sales_amount_6_m = None
        self._sales_amount_mom = None
        self._sales_amount_p_12_m_mom = None
        self._sales_amount_p_12_m_yoy = None
        self._sales_amount_p_3_m_mom = None
        self._sales_amount_p_3_m_yoy = None
        self._sales_amount_p_6_m_mom = None
        self._sales_amount_p_6_m_yoy = None
        self._sales_amount_yoy = None

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value
    @property
    def sales_amount_12_m(self):
        return self._sales_amount_12_m

    @sales_amount_12_m.setter
    def sales_amount_12_m(self, value):
        self._sales_amount_12_m = value
    @property
    def sales_amount_1_m(self):
        return self._sales_amount_1_m

    @sales_amount_1_m.setter
    def sales_amount_1_m(self, value):
        self._sales_amount_1_m = value
    @property
    def sales_amount_3_m(self):
        return self._sales_amount_3_m

    @sales_amount_3_m.setter
    def sales_amount_3_m(self, value):
        self._sales_amount_3_m = value
    @property
    def sales_amount_6_m(self):
        return self._sales_amount_6_m

    @sales_amount_6_m.setter
    def sales_amount_6_m(self, value):
        self._sales_amount_6_m = value
    @property
    def sales_amount_mom(self):
        return self._sales_amount_mom

    @sales_amount_mom.setter
    def sales_amount_mom(self, value):
        self._sales_amount_mom = value
    @property
    def sales_amount_p_12_m_mom(self):
        return self._sales_amount_p_12_m_mom

    @sales_amount_p_12_m_mom.setter
    def sales_amount_p_12_m_mom(self, value):
        self._sales_amount_p_12_m_mom = value
    @property
    def sales_amount_p_12_m_yoy(self):
        return self._sales_amount_p_12_m_yoy

    @sales_amount_p_12_m_yoy.setter
    def sales_amount_p_12_m_yoy(self, value):
        self._sales_amount_p_12_m_yoy = value
    @property
    def sales_amount_p_3_m_mom(self):
        return self._sales_amount_p_3_m_mom

    @sales_amount_p_3_m_mom.setter
    def sales_amount_p_3_m_mom(self, value):
        self._sales_amount_p_3_m_mom = value
    @property
    def sales_amount_p_3_m_yoy(self):
        return self._sales_amount_p_3_m_yoy

    @sales_amount_p_3_m_yoy.setter
    def sales_amount_p_3_m_yoy(self, value):
        self._sales_amount_p_3_m_yoy = value
    @property
    def sales_amount_p_6_m_mom(self):
        return self._sales_amount_p_6_m_mom

    @sales_amount_p_6_m_mom.setter
    def sales_amount_p_6_m_mom(self, value):
        self._sales_amount_p_6_m_mom = value
    @property
    def sales_amount_p_6_m_yoy(self):
        return self._sales_amount_p_6_m_yoy

    @sales_amount_p_6_m_yoy.setter
    def sales_amount_p_6_m_yoy(self, value):
        self._sales_amount_p_6_m_yoy = value
    @property
    def sales_amount_yoy(self):
        return self._sales_amount_yoy

    @sales_amount_yoy.setter
    def sales_amount_yoy(self, value):
        self._sales_amount_yoy = value


    def to_alipay_dict(self):
        params = dict()
        if self.month:
            if hasattr(self.month, 'to_alipay_dict'):
                params['month'] = self.month.to_alipay_dict()
            else:
                params['month'] = self.month
        if self.sales_amount_12_m:
            if hasattr(self.sales_amount_12_m, 'to_alipay_dict'):
                params['sales_amount_12_m'] = self.sales_amount_12_m.to_alipay_dict()
            else:
                params['sales_amount_12_m'] = self.sales_amount_12_m
        if self.sales_amount_1_m:
            if hasattr(self.sales_amount_1_m, 'to_alipay_dict'):
                params['sales_amount_1_m'] = self.sales_amount_1_m.to_alipay_dict()
            else:
                params['sales_amount_1_m'] = self.sales_amount_1_m
        if self.sales_amount_3_m:
            if hasattr(self.sales_amount_3_m, 'to_alipay_dict'):
                params['sales_amount_3_m'] = self.sales_amount_3_m.to_alipay_dict()
            else:
                params['sales_amount_3_m'] = self.sales_amount_3_m
        if self.sales_amount_6_m:
            if hasattr(self.sales_amount_6_m, 'to_alipay_dict'):
                params['sales_amount_6_m'] = self.sales_amount_6_m.to_alipay_dict()
            else:
                params['sales_amount_6_m'] = self.sales_amount_6_m
        if self.sales_amount_mom:
            if hasattr(self.sales_amount_mom, 'to_alipay_dict'):
                params['sales_amount_mom'] = self.sales_amount_mom.to_alipay_dict()
            else:
                params['sales_amount_mom'] = self.sales_amount_mom
        if self.sales_amount_p_12_m_mom:
            if hasattr(self.sales_amount_p_12_m_mom, 'to_alipay_dict'):
                params['sales_amount_p_12_m_mom'] = self.sales_amount_p_12_m_mom.to_alipay_dict()
            else:
                params['sales_amount_p_12_m_mom'] = self.sales_amount_p_12_m_mom
        if self.sales_amount_p_12_m_yoy:
            if hasattr(self.sales_amount_p_12_m_yoy, 'to_alipay_dict'):
                params['sales_amount_p_12_m_yoy'] = self.sales_amount_p_12_m_yoy.to_alipay_dict()
            else:
                params['sales_amount_p_12_m_yoy'] = self.sales_amount_p_12_m_yoy
        if self.sales_amount_p_3_m_mom:
            if hasattr(self.sales_amount_p_3_m_mom, 'to_alipay_dict'):
                params['sales_amount_p_3_m_mom'] = self.sales_amount_p_3_m_mom.to_alipay_dict()
            else:
                params['sales_amount_p_3_m_mom'] = self.sales_amount_p_3_m_mom
        if self.sales_amount_p_3_m_yoy:
            if hasattr(self.sales_amount_p_3_m_yoy, 'to_alipay_dict'):
                params['sales_amount_p_3_m_yoy'] = self.sales_amount_p_3_m_yoy.to_alipay_dict()
            else:
                params['sales_amount_p_3_m_yoy'] = self.sales_amount_p_3_m_yoy
        if self.sales_amount_p_6_m_mom:
            if hasattr(self.sales_amount_p_6_m_mom, 'to_alipay_dict'):
                params['sales_amount_p_6_m_mom'] = self.sales_amount_p_6_m_mom.to_alipay_dict()
            else:
                params['sales_amount_p_6_m_mom'] = self.sales_amount_p_6_m_mom
        if self.sales_amount_p_6_m_yoy:
            if hasattr(self.sales_amount_p_6_m_yoy, 'to_alipay_dict'):
                params['sales_amount_p_6_m_yoy'] = self.sales_amount_p_6_m_yoy.to_alipay_dict()
            else:
                params['sales_amount_p_6_m_yoy'] = self.sales_amount_p_6_m_yoy
        if self.sales_amount_yoy:
            if hasattr(self.sales_amount_yoy, 'to_alipay_dict'):
                params['sales_amount_yoy'] = self.sales_amount_yoy.to_alipay_dict()
            else:
                params['sales_amount_yoy'] = self.sales_amount_yoy
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FrShopIndexInfo()
        if 'month' in d:
            o.month = d['month']
        if 'sales_amount_12_m' in d:
            o.sales_amount_12_m = d['sales_amount_12_m']
        if 'sales_amount_1_m' in d:
            o.sales_amount_1_m = d['sales_amount_1_m']
        if 'sales_amount_3_m' in d:
            o.sales_amount_3_m = d['sales_amount_3_m']
        if 'sales_amount_6_m' in d:
            o.sales_amount_6_m = d['sales_amount_6_m']
        if 'sales_amount_mom' in d:
            o.sales_amount_mom = d['sales_amount_mom']
        if 'sales_amount_p_12_m_mom' in d:
            o.sales_amount_p_12_m_mom = d['sales_amount_p_12_m_mom']
        if 'sales_amount_p_12_m_yoy' in d:
            o.sales_amount_p_12_m_yoy = d['sales_amount_p_12_m_yoy']
        if 'sales_amount_p_3_m_mom' in d:
            o.sales_amount_p_3_m_mom = d['sales_amount_p_3_m_mom']
        if 'sales_amount_p_3_m_yoy' in d:
            o.sales_amount_p_3_m_yoy = d['sales_amount_p_3_m_yoy']
        if 'sales_amount_p_6_m_mom' in d:
            o.sales_amount_p_6_m_mom = d['sales_amount_p_6_m_mom']
        if 'sales_amount_p_6_m_yoy' in d:
            o.sales_amount_p_6_m_yoy = d['sales_amount_p_6_m_yoy']
        if 'sales_amount_yoy' in d:
            o.sales_amount_yoy = d['sales_amount_yoy']
        return o


