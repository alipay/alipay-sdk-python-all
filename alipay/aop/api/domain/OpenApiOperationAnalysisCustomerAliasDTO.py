#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO


class OpenApiOperationAnalysisCustomerAliasDTO(object):

    def __init__(self):
        self._alipay_app_id = None
        self._alipay_app_name = None
        self._channel_type = None
        self._dt = None
        self._multi_app_id = None
        self._multi_app_name = None
        self._order_traded_user_cvr = None
        self._tapp_order_user_cnt = None
        self._tapp_traded_user_cnt = None
        self._traded_user_cvr = None
        self._user_type = None
        self._uv = None
        self._visit_order_user_cvr = None

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
    def order_traded_user_cvr(self):
        return self._order_traded_user_cvr

    @order_traded_user_cvr.setter
    def order_traded_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._order_traded_user_cvr = value
        else:
            self._order_traded_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def tapp_order_user_cnt(self):
        return self._tapp_order_user_cnt

    @tapp_order_user_cnt.setter
    def tapp_order_user_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._tapp_order_user_cnt = value
        else:
            self._tapp_order_user_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def tapp_traded_user_cnt(self):
        return self._tapp_traded_user_cnt

    @tapp_traded_user_cnt.setter
    def tapp_traded_user_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._tapp_traded_user_cnt = value
        else:
            self._tapp_traded_user_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def traded_user_cvr(self):
        return self._traded_user_cvr

    @traded_user_cvr.setter
    def traded_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._traded_user_cvr = value
        else:
            self._traded_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value
    @property
    def uv(self):
        return self._uv

    @uv.setter
    def uv(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._uv = value
        else:
            self._uv = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def visit_order_user_cvr(self):
        return self._visit_order_user_cvr

    @visit_order_user_cvr.setter
    def visit_order_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._visit_order_user_cvr = value
        else:
            self._visit_order_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)


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
        if self.order_traded_user_cvr:
            if hasattr(self.order_traded_user_cvr, 'to_alipay_dict'):
                params['order_traded_user_cvr'] = self.order_traded_user_cvr.to_alipay_dict()
            else:
                params['order_traded_user_cvr'] = self.order_traded_user_cvr
        if self.tapp_order_user_cnt:
            if hasattr(self.tapp_order_user_cnt, 'to_alipay_dict'):
                params['tapp_order_user_cnt'] = self.tapp_order_user_cnt.to_alipay_dict()
            else:
                params['tapp_order_user_cnt'] = self.tapp_order_user_cnt
        if self.tapp_traded_user_cnt:
            if hasattr(self.tapp_traded_user_cnt, 'to_alipay_dict'):
                params['tapp_traded_user_cnt'] = self.tapp_traded_user_cnt.to_alipay_dict()
            else:
                params['tapp_traded_user_cnt'] = self.tapp_traded_user_cnt
        if self.traded_user_cvr:
            if hasattr(self.traded_user_cvr, 'to_alipay_dict'):
                params['traded_user_cvr'] = self.traded_user_cvr.to_alipay_dict()
            else:
                params['traded_user_cvr'] = self.traded_user_cvr
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        if self.uv:
            if hasattr(self.uv, 'to_alipay_dict'):
                params['uv'] = self.uv.to_alipay_dict()
            else:
                params['uv'] = self.uv
        if self.visit_order_user_cvr:
            if hasattr(self.visit_order_user_cvr, 'to_alipay_dict'):
                params['visit_order_user_cvr'] = self.visit_order_user_cvr.to_alipay_dict()
            else:
                params['visit_order_user_cvr'] = self.visit_order_user_cvr
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiOperationAnalysisCustomerAliasDTO()
        if 'alipay_app_id' in d:
            o.alipay_app_id = d['alipay_app_id']
        if 'alipay_app_name' in d:
            o.alipay_app_name = d['alipay_app_name']
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'dt' in d:
            o.dt = d['dt']
        if 'multi_app_id' in d:
            o.multi_app_id = d['multi_app_id']
        if 'multi_app_name' in d:
            o.multi_app_name = d['multi_app_name']
        if 'order_traded_user_cvr' in d:
            o.order_traded_user_cvr = d['order_traded_user_cvr']
        if 'tapp_order_user_cnt' in d:
            o.tapp_order_user_cnt = d['tapp_order_user_cnt']
        if 'tapp_traded_user_cnt' in d:
            o.tapp_traded_user_cnt = d['tapp_traded_user_cnt']
        if 'traded_user_cvr' in d:
            o.traded_user_cvr = d['traded_user_cvr']
        if 'user_type' in d:
            o.user_type = d['user_type']
        if 'uv' in d:
            o.uv = d['uv']
        if 'visit_order_user_cvr' in d:
            o.visit_order_user_cvr = d['visit_order_user_cvr']
        return o


