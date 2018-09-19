#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubCertDetail(object):

    def __init__(self):
        self._lot_num = None
        self._lot_point = None
        self._sub_lotnum = None

    @property
    def lot_num(self):
        return self._lot_num

    @lot_num.setter
    def lot_num(self, value):
        self._lot_num = value
    @property
    def lot_point(self):
        return self._lot_point

    @lot_point.setter
    def lot_point(self, value):
        self._lot_point = value
    @property
    def sub_lotnum(self):
        return self._sub_lotnum

    @sub_lotnum.setter
    def sub_lotnum(self, value):
        self._sub_lotnum = value


    def to_alipay_dict(self):
        params = dict()
        if self.lot_num:
            if hasattr(self.lot_num, 'to_alipay_dict'):
                params['lot_num'] = self.lot_num.to_alipay_dict()
            else:
                params['lot_num'] = self.lot_num
        if self.lot_point:
            if hasattr(self.lot_point, 'to_alipay_dict'):
                params['lot_point'] = self.lot_point.to_alipay_dict()
            else:
                params['lot_point'] = self.lot_point
        if self.sub_lotnum:
            if hasattr(self.sub_lotnum, 'to_alipay_dict'):
                params['sub_lotnum'] = self.sub_lotnum.to_alipay_dict()
            else:
                params['sub_lotnum'] = self.sub_lotnum
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubCertDetail()
        if 'lot_num' in d:
            o.lot_num = d['lot_num']
        if 'lot_point' in d:
            o.lot_point = d['lot_point']
        if 'sub_lotnum' in d:
            o.sub_lotnum = d['sub_lotnum']
        return o


