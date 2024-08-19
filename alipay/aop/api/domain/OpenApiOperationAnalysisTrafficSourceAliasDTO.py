#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO


class OpenApiOperationAnalysisTrafficSourceAliasDTO(object):

    def __init__(self):
        self._alipay_app_id = None
        self._alipay_app_name = None
        self._channel_type = None
        self._dt = None
        self._first_source_type = None
        self._multi_app_id = None
        self._multi_app_name = None
        self._second_source_type = None
        self._tapp_add_user_cnt = None
        self._tapp_order_traded_user_cvr = None
        self._tapp_order_user_cnt = None
        self._tapp_traded_user_cnt = None
        self._tapp_uv = None
        self._tapp_uv_rate = None
        self._tapp_visit_order_user_cvr = None
        self._tapp_visit_traded_user_cvr = None

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
    def first_source_type(self):
        return self._first_source_type

    @first_source_type.setter
    def first_source_type(self, value):
        self._first_source_type = value
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
    def second_source_type(self):
        return self._second_source_type

    @second_source_type.setter
    def second_source_type(self, value):
        self._second_source_type = value
    @property
    def tapp_add_user_cnt(self):
        return self._tapp_add_user_cnt

    @tapp_add_user_cnt.setter
    def tapp_add_user_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._tapp_add_user_cnt = value
        else:
            self._tapp_add_user_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def tapp_order_traded_user_cvr(self):
        return self._tapp_order_traded_user_cvr

    @tapp_order_traded_user_cvr.setter
    def tapp_order_traded_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._tapp_order_traded_user_cvr = value
        else:
            self._tapp_order_traded_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)
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
    def tapp_uv(self):
        return self._tapp_uv

    @tapp_uv.setter
    def tapp_uv(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._tapp_uv = value
        else:
            self._tapp_uv = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def tapp_uv_rate(self):
        return self._tapp_uv_rate

    @tapp_uv_rate.setter
    def tapp_uv_rate(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._tapp_uv_rate = value
        else:
            self._tapp_uv_rate = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def tapp_visit_order_user_cvr(self):
        return self._tapp_visit_order_user_cvr

    @tapp_visit_order_user_cvr.setter
    def tapp_visit_order_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._tapp_visit_order_user_cvr = value
        else:
            self._tapp_visit_order_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def tapp_visit_traded_user_cvr(self):
        return self._tapp_visit_traded_user_cvr

    @tapp_visit_traded_user_cvr.setter
    def tapp_visit_traded_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._tapp_visit_traded_user_cvr = value
        else:
            self._tapp_visit_traded_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)


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
        if self.first_source_type:
            if hasattr(self.first_source_type, 'to_alipay_dict'):
                params['first_source_type'] = self.first_source_type.to_alipay_dict()
            else:
                params['first_source_type'] = self.first_source_type
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
        if self.second_source_type:
            if hasattr(self.second_source_type, 'to_alipay_dict'):
                params['second_source_type'] = self.second_source_type.to_alipay_dict()
            else:
                params['second_source_type'] = self.second_source_type
        if self.tapp_add_user_cnt:
            if hasattr(self.tapp_add_user_cnt, 'to_alipay_dict'):
                params['tapp_add_user_cnt'] = self.tapp_add_user_cnt.to_alipay_dict()
            else:
                params['tapp_add_user_cnt'] = self.tapp_add_user_cnt
        if self.tapp_order_traded_user_cvr:
            if hasattr(self.tapp_order_traded_user_cvr, 'to_alipay_dict'):
                params['tapp_order_traded_user_cvr'] = self.tapp_order_traded_user_cvr.to_alipay_dict()
            else:
                params['tapp_order_traded_user_cvr'] = self.tapp_order_traded_user_cvr
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
        if self.tapp_uv:
            if hasattr(self.tapp_uv, 'to_alipay_dict'):
                params['tapp_uv'] = self.tapp_uv.to_alipay_dict()
            else:
                params['tapp_uv'] = self.tapp_uv
        if self.tapp_uv_rate:
            if hasattr(self.tapp_uv_rate, 'to_alipay_dict'):
                params['tapp_uv_rate'] = self.tapp_uv_rate.to_alipay_dict()
            else:
                params['tapp_uv_rate'] = self.tapp_uv_rate
        if self.tapp_visit_order_user_cvr:
            if hasattr(self.tapp_visit_order_user_cvr, 'to_alipay_dict'):
                params['tapp_visit_order_user_cvr'] = self.tapp_visit_order_user_cvr.to_alipay_dict()
            else:
                params['tapp_visit_order_user_cvr'] = self.tapp_visit_order_user_cvr
        if self.tapp_visit_traded_user_cvr:
            if hasattr(self.tapp_visit_traded_user_cvr, 'to_alipay_dict'):
                params['tapp_visit_traded_user_cvr'] = self.tapp_visit_traded_user_cvr.to_alipay_dict()
            else:
                params['tapp_visit_traded_user_cvr'] = self.tapp_visit_traded_user_cvr
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiOperationAnalysisTrafficSourceAliasDTO()
        if 'alipay_app_id' in d:
            o.alipay_app_id = d['alipay_app_id']
        if 'alipay_app_name' in d:
            o.alipay_app_name = d['alipay_app_name']
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'dt' in d:
            o.dt = d['dt']
        if 'first_source_type' in d:
            o.first_source_type = d['first_source_type']
        if 'multi_app_id' in d:
            o.multi_app_id = d['multi_app_id']
        if 'multi_app_name' in d:
            o.multi_app_name = d['multi_app_name']
        if 'second_source_type' in d:
            o.second_source_type = d['second_source_type']
        if 'tapp_add_user_cnt' in d:
            o.tapp_add_user_cnt = d['tapp_add_user_cnt']
        if 'tapp_order_traded_user_cvr' in d:
            o.tapp_order_traded_user_cvr = d['tapp_order_traded_user_cvr']
        if 'tapp_order_user_cnt' in d:
            o.tapp_order_user_cnt = d['tapp_order_user_cnt']
        if 'tapp_traded_user_cnt' in d:
            o.tapp_traded_user_cnt = d['tapp_traded_user_cnt']
        if 'tapp_uv' in d:
            o.tapp_uv = d['tapp_uv']
        if 'tapp_uv_rate' in d:
            o.tapp_uv_rate = d['tapp_uv_rate']
        if 'tapp_visit_order_user_cvr' in d:
            o.tapp_visit_order_user_cvr = d['tapp_visit_order_user_cvr']
        if 'tapp_visit_traded_user_cvr' in d:
            o.tapp_visit_traded_user_cvr = d['tapp_visit_traded_user_cvr']
        return o


