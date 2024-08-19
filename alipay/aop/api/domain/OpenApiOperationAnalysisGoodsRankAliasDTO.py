#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO


class OpenApiOperationAnalysisGoodsRankAliasDTO(object):

    def __init__(self):
        self._alipay_app_id = None
        self._alipay_app_name = None
        self._cate_id = None
        self._cate_name = None
        self._channel_type = None
        self._dt = None
        self._multi_app_id = None
        self._multi_app_name = None
        self._spu_id = None
        self._spu_name = None
        self._spu_traded_amt = None
        self._spu_traded_refund_amt = None
        self._spu_traded_sales_cnt = None
        self._spu_uv = None

    @property
    def alipay_app_id(self):
        return self._alipay_app_id

    @alipay_app_id.setter
    def alipay_app_id(self, value):
        self._alipay_app_id = value
    @property
    def alipay_app_name(self):
        return self._alipay_app_name

    @alipay_app_name.setter
    def alipay_app_name(self, value):
        self._alipay_app_name = value
    @property
    def cate_id(self):
        return self._cate_id

    @cate_id.setter
    def cate_id(self, value):
        self._cate_id = value
    @property
    def cate_name(self):
        return self._cate_name

    @cate_name.setter
    def cate_name(self, value):
        self._cate_name = value
    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def dt(self):
        return self._dt

    @dt.setter
    def dt(self, value):
        self._dt = value
    @property
    def multi_app_id(self):
        return self._multi_app_id

    @multi_app_id.setter
    def multi_app_id(self, value):
        self._multi_app_id = value
    @property
    def multi_app_name(self):
        return self._multi_app_name

    @multi_app_name.setter
    def multi_app_name(self, value):
        self._multi_app_name = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value
    @property
    def spu_name(self):
        return self._spu_name

    @spu_name.setter
    def spu_name(self, value):
        self._spu_name = value
    @property
    def spu_traded_amt(self):
        return self._spu_traded_amt

    @spu_traded_amt.setter
    def spu_traded_amt(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._spu_traded_amt = value
        else:
            self._spu_traded_amt = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def spu_traded_refund_amt(self):
        return self._spu_traded_refund_amt

    @spu_traded_refund_amt.setter
    def spu_traded_refund_amt(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._spu_traded_refund_amt = value
        else:
            self._spu_traded_refund_amt = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def spu_traded_sales_cnt(self):
        return self._spu_traded_sales_cnt

    @spu_traded_sales_cnt.setter
    def spu_traded_sales_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._spu_traded_sales_cnt = value
        else:
            self._spu_traded_sales_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def spu_uv(self):
        return self._spu_uv

    @spu_uv.setter
    def spu_uv(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._spu_uv = value
        else:
            self._spu_uv = OperationValueLongDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_app_id:
            if hasattr(self.alipay_app_id, 'to_alipay_dict'):
                params['alipay_app_id'] = self.alipay_app_id.to_alipay_dict()
            else:
                params['alipay_app_id'] = self.alipay_app_id
        if self.alipay_app_name:
            if hasattr(self.alipay_app_name, 'to_alipay_dict'):
                params['alipay_app_name'] = self.alipay_app_name.to_alipay_dict()
            else:
                params['alipay_app_name'] = self.alipay_app_name
        if self.cate_id:
            if hasattr(self.cate_id, 'to_alipay_dict'):
                params['cate_id'] = self.cate_id.to_alipay_dict()
            else:
                params['cate_id'] = self.cate_id
        if self.cate_name:
            if hasattr(self.cate_name, 'to_alipay_dict'):
                params['cate_name'] = self.cate_name.to_alipay_dict()
            else:
                params['cate_name'] = self.cate_name
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        if self.dt:
            if hasattr(self.dt, 'to_alipay_dict'):
                params['dt'] = self.dt.to_alipay_dict()
            else:
                params['dt'] = self.dt
        if self.multi_app_id:
            if hasattr(self.multi_app_id, 'to_alipay_dict'):
                params['multi_app_id'] = self.multi_app_id.to_alipay_dict()
            else:
                params['multi_app_id'] = self.multi_app_id
        if self.multi_app_name:
            if hasattr(self.multi_app_name, 'to_alipay_dict'):
                params['multi_app_name'] = self.multi_app_name.to_alipay_dict()
            else:
                params['multi_app_name'] = self.multi_app_name
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
        if self.spu_name:
            if hasattr(self.spu_name, 'to_alipay_dict'):
                params['spu_name'] = self.spu_name.to_alipay_dict()
            else:
                params['spu_name'] = self.spu_name
        if self.spu_traded_amt:
            if hasattr(self.spu_traded_amt, 'to_alipay_dict'):
                params['spu_traded_amt'] = self.spu_traded_amt.to_alipay_dict()
            else:
                params['spu_traded_amt'] = self.spu_traded_amt
        if self.spu_traded_refund_amt:
            if hasattr(self.spu_traded_refund_amt, 'to_alipay_dict'):
                params['spu_traded_refund_amt'] = self.spu_traded_refund_amt.to_alipay_dict()
            else:
                params['spu_traded_refund_amt'] = self.spu_traded_refund_amt
        if self.spu_traded_sales_cnt:
            if hasattr(self.spu_traded_sales_cnt, 'to_alipay_dict'):
                params['spu_traded_sales_cnt'] = self.spu_traded_sales_cnt.to_alipay_dict()
            else:
                params['spu_traded_sales_cnt'] = self.spu_traded_sales_cnt
        if self.spu_uv:
            if hasattr(self.spu_uv, 'to_alipay_dict'):
                params['spu_uv'] = self.spu_uv.to_alipay_dict()
            else:
                params['spu_uv'] = self.spu_uv
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiOperationAnalysisGoodsRankAliasDTO()
        if 'alipay_app_id' in d:
            o.alipay_app_id = d['alipay_app_id']
        if 'alipay_app_name' in d:
            o.alipay_app_name = d['alipay_app_name']
        if 'cate_id' in d:
            o.cate_id = d['cate_id']
        if 'cate_name' in d:
            o.cate_name = d['cate_name']
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'dt' in d:
            o.dt = d['dt']
        if 'multi_app_id' in d:
            o.multi_app_id = d['multi_app_id']
        if 'multi_app_name' in d:
            o.multi_app_name = d['multi_app_name']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        if 'spu_name' in d:
            o.spu_name = d['spu_name']
        if 'spu_traded_amt' in d:
            o.spu_traded_amt = d['spu_traded_amt']
        if 'spu_traded_refund_amt' in d:
            o.spu_traded_refund_amt = d['spu_traded_refund_amt']
        if 'spu_traded_sales_cnt' in d:
            o.spu_traded_sales_cnt = d['spu_traded_sales_cnt']
        if 'spu_uv' in d:
            o.spu_uv = d['spu_uv']
        return o


