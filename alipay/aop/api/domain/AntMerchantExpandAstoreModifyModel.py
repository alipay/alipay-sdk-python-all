#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SettleInfoModel import SettleInfoModel


class AntMerchantExpandAstoreModifyModel(object):

    def __init__(self):
        self._a_store_id = None
        self._mobile = None
        self._settle_infos = None

    @property
    def a_store_id(self):
        return self._a_store_id

    @a_store_id.setter
    def a_store_id(self, value):
        self._a_store_id = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def settle_infos(self):
        return self._settle_infos

    @settle_infos.setter
    def settle_infos(self, value):
        if isinstance(value, SettleInfoModel):
            self._settle_infos = value
        else:
            self._settle_infos = SettleInfoModel.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.a_store_id:
            if hasattr(self.a_store_id, 'to_alipay_dict'):
                params['a_store_id'] = self.a_store_id.to_alipay_dict()
            else:
                params['a_store_id'] = self.a_store_id
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.settle_infos:
            if hasattr(self.settle_infos, 'to_alipay_dict'):
                params['settle_infos'] = self.settle_infos.to_alipay_dict()
            else:
                params['settle_infos'] = self.settle_infos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandAstoreModifyModel()
        if 'a_store_id' in d:
            o.a_store_id = d['a_store_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'settle_infos' in d:
            o.settle_infos = d['settle_infos']
        return o


