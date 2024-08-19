#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO


class OpenApiOperationAnalysisTrafficAliasDTO(object):

    def __init__(self):
        self._alipay_app_id = None
        self._alipay_app_name = None
        self._channel_type = None
        self._dt = None
        self._multi_app_id = None
        self._multi_app_name = None
        self._per_customer_price = None
        self._per_unit_price = None
        self._tapp_add_order_cnt = None
        self._tapp_add_sku_cnt = None
        self._tapp_add_user_cnt = None
        self._tapp_new_uv = None
        self._tapp_old_uv = None
        self._tapp_order_amt = None
        self._tapp_order_cnt = None
        self._tapp_order_user_cnt = None
        self._tapp_pv = None
        self._tapp_refund_amt = None
        self._tapp_refund_cnt = None
        self._tapp_refund_user_cnt = None
        self._tapp_traded_amt = None
        self._tapp_traded_cnt = None
        self._tapp_traded_refund_user_cvr = None
        self._tapp_traded_user_cnt = None
        self._tapp_untraded_amt = None
        self._tapp_untraded_cnt = None
        self._tapp_untraded_user_cnt = None
        self._tapp_uv = None
        self._tapp_visit_add_user_cvr = None
        self._tapp_visit_order_user_cvr = None
        self._tapp_visit_traded_user_cvr = None
        self._tapp_visit_untraded_user_cvr = None

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
    def per_customer_price(self):
        return self._per_customer_price

    @per_customer_price.setter
    def per_customer_price(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._per_customer_price = value
        else:
            self._per_customer_price = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def per_unit_price(self):
        return self._per_unit_price

    @per_unit_price.setter
    def per_unit_price(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._per_unit_price = value
        else:
            self._per_unit_price = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def tapp_add_order_cnt(self):
        return self._tapp_add_order_cnt

    @tapp_add_order_cnt.setter
    def tapp_add_order_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._tapp_add_order_cnt = value
        else:
            self._tapp_add_order_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def tapp_add_sku_cnt(self):
        return self._tapp_add_sku_cnt

    @tapp_add_sku_cnt.setter
    def tapp_add_sku_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._tapp_add_sku_cnt = value
        else:
            self._tapp_add_sku_cnt = OperationValueLongDTO.from_alipay_dict(value)
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
    def tapp_new_uv(self):
        return self._tapp_new_uv

    @tapp_new_uv.setter
    def tapp_new_uv(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._tapp_new_uv = value
        else:
            self._tapp_new_uv = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def tapp_old_uv(self):
        return self._tapp_old_uv

    @tapp_old_uv.setter
    def tapp_old_uv(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._tapp_old_uv = value
        else:
            self._tapp_old_uv = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def tapp_order_amt(self):
        return self._tapp_order_amt

    @tapp_order_amt.setter
    def tapp_order_amt(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._tapp_order_amt = value
        else:
            self._tapp_order_amt = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def tapp_order_cnt(self):
        return self._tapp_order_cnt

    @tapp_order_cnt.setter
    def tapp_order_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._tapp_order_cnt = value
        else:
            self._tapp_order_cnt = OperationValueLongDTO.from_alipay_dict(value)
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
    def tapp_pv(self):
        return self._tapp_pv

    @tapp_pv.setter
    def tapp_pv(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._tapp_pv = value
        else:
            self._tapp_pv = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def tapp_refund_amt(self):
        return self._tapp_refund_amt

    @tapp_refund_amt.setter
    def tapp_refund_amt(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._tapp_refund_amt = value
        else:
            self._tapp_refund_amt = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def tapp_refund_cnt(self):
        return self._tapp_refund_cnt

    @tapp_refund_cnt.setter
    def tapp_refund_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._tapp_refund_cnt = value
        else:
            self._tapp_refund_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def tapp_refund_user_cnt(self):
        return self._tapp_refund_user_cnt

    @tapp_refund_user_cnt.setter
    def tapp_refund_user_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._tapp_refund_user_cnt = value
        else:
            self._tapp_refund_user_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def tapp_traded_amt(self):
        return self._tapp_traded_amt

    @tapp_traded_amt.setter
    def tapp_traded_amt(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._tapp_traded_amt = value
        else:
            self._tapp_traded_amt = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def tapp_traded_cnt(self):
        return self._tapp_traded_cnt

    @tapp_traded_cnt.setter
    def tapp_traded_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._tapp_traded_cnt = value
        else:
            self._tapp_traded_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def tapp_traded_refund_user_cvr(self):
        return self._tapp_traded_refund_user_cvr

    @tapp_traded_refund_user_cvr.setter
    def tapp_traded_refund_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._tapp_traded_refund_user_cvr = value
        else:
            self._tapp_traded_refund_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)
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
    def tapp_untraded_amt(self):
        return self._tapp_untraded_amt

    @tapp_untraded_amt.setter
    def tapp_untraded_amt(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._tapp_untraded_amt = value
        else:
            self._tapp_untraded_amt = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def tapp_untraded_cnt(self):
        return self._tapp_untraded_cnt

    @tapp_untraded_cnt.setter
    def tapp_untraded_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._tapp_untraded_cnt = value
        else:
            self._tapp_untraded_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def tapp_untraded_user_cnt(self):
        return self._tapp_untraded_user_cnt

    @tapp_untraded_user_cnt.setter
    def tapp_untraded_user_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._tapp_untraded_user_cnt = value
        else:
            self._tapp_untraded_user_cnt = OperationValueLongDTO.from_alipay_dict(value)
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
    def tapp_visit_add_user_cvr(self):
        return self._tapp_visit_add_user_cvr

    @tapp_visit_add_user_cvr.setter
    def tapp_visit_add_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._tapp_visit_add_user_cvr = value
        else:
            self._tapp_visit_add_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)
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
    @property
    def tapp_visit_untraded_user_cvr(self):
        return self._tapp_visit_untraded_user_cvr

    @tapp_visit_untraded_user_cvr.setter
    def tapp_visit_untraded_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._tapp_visit_untraded_user_cvr = value
        else:
            self._tapp_visit_untraded_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)


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
        if self.per_customer_price:
            if hasattr(self.per_customer_price, 'to_alipay_dict'):
                params['per_customer_price'] = self.per_customer_price.to_alipay_dict()
            else:
                params['per_customer_price'] = self.per_customer_price
        if self.per_unit_price:
            if hasattr(self.per_unit_price, 'to_alipay_dict'):
                params['per_unit_price'] = self.per_unit_price.to_alipay_dict()
            else:
                params['per_unit_price'] = self.per_unit_price
        if self.tapp_add_order_cnt:
            if hasattr(self.tapp_add_order_cnt, 'to_alipay_dict'):
                params['tapp_add_order_cnt'] = self.tapp_add_order_cnt.to_alipay_dict()
            else:
                params['tapp_add_order_cnt'] = self.tapp_add_order_cnt
        if self.tapp_add_sku_cnt:
            if hasattr(self.tapp_add_sku_cnt, 'to_alipay_dict'):
                params['tapp_add_sku_cnt'] = self.tapp_add_sku_cnt.to_alipay_dict()
            else:
                params['tapp_add_sku_cnt'] = self.tapp_add_sku_cnt
        if self.tapp_add_user_cnt:
            if hasattr(self.tapp_add_user_cnt, 'to_alipay_dict'):
                params['tapp_add_user_cnt'] = self.tapp_add_user_cnt.to_alipay_dict()
            else:
                params['tapp_add_user_cnt'] = self.tapp_add_user_cnt
        if self.tapp_new_uv:
            if hasattr(self.tapp_new_uv, 'to_alipay_dict'):
                params['tapp_new_uv'] = self.tapp_new_uv.to_alipay_dict()
            else:
                params['tapp_new_uv'] = self.tapp_new_uv
        if self.tapp_old_uv:
            if hasattr(self.tapp_old_uv, 'to_alipay_dict'):
                params['tapp_old_uv'] = self.tapp_old_uv.to_alipay_dict()
            else:
                params['tapp_old_uv'] = self.tapp_old_uv
        if self.tapp_order_amt:
            if hasattr(self.tapp_order_amt, 'to_alipay_dict'):
                params['tapp_order_amt'] = self.tapp_order_amt.to_alipay_dict()
            else:
                params['tapp_order_amt'] = self.tapp_order_amt
        if self.tapp_order_cnt:
            if hasattr(self.tapp_order_cnt, 'to_alipay_dict'):
                params['tapp_order_cnt'] = self.tapp_order_cnt.to_alipay_dict()
            else:
                params['tapp_order_cnt'] = self.tapp_order_cnt
        if self.tapp_order_user_cnt:
            if hasattr(self.tapp_order_user_cnt, 'to_alipay_dict'):
                params['tapp_order_user_cnt'] = self.tapp_order_user_cnt.to_alipay_dict()
            else:
                params['tapp_order_user_cnt'] = self.tapp_order_user_cnt
        if self.tapp_pv:
            if hasattr(self.tapp_pv, 'to_alipay_dict'):
                params['tapp_pv'] = self.tapp_pv.to_alipay_dict()
            else:
                params['tapp_pv'] = self.tapp_pv
        if self.tapp_refund_amt:
            if hasattr(self.tapp_refund_amt, 'to_alipay_dict'):
                params['tapp_refund_amt'] = self.tapp_refund_amt.to_alipay_dict()
            else:
                params['tapp_refund_amt'] = self.tapp_refund_amt
        if self.tapp_refund_cnt:
            if hasattr(self.tapp_refund_cnt, 'to_alipay_dict'):
                params['tapp_refund_cnt'] = self.tapp_refund_cnt.to_alipay_dict()
            else:
                params['tapp_refund_cnt'] = self.tapp_refund_cnt
        if self.tapp_refund_user_cnt:
            if hasattr(self.tapp_refund_user_cnt, 'to_alipay_dict'):
                params['tapp_refund_user_cnt'] = self.tapp_refund_user_cnt.to_alipay_dict()
            else:
                params['tapp_refund_user_cnt'] = self.tapp_refund_user_cnt
        if self.tapp_traded_amt:
            if hasattr(self.tapp_traded_amt, 'to_alipay_dict'):
                params['tapp_traded_amt'] = self.tapp_traded_amt.to_alipay_dict()
            else:
                params['tapp_traded_amt'] = self.tapp_traded_amt
        if self.tapp_traded_cnt:
            if hasattr(self.tapp_traded_cnt, 'to_alipay_dict'):
                params['tapp_traded_cnt'] = self.tapp_traded_cnt.to_alipay_dict()
            else:
                params['tapp_traded_cnt'] = self.tapp_traded_cnt
        if self.tapp_traded_refund_user_cvr:
            if hasattr(self.tapp_traded_refund_user_cvr, 'to_alipay_dict'):
                params['tapp_traded_refund_user_cvr'] = self.tapp_traded_refund_user_cvr.to_alipay_dict()
            else:
                params['tapp_traded_refund_user_cvr'] = self.tapp_traded_refund_user_cvr
        if self.tapp_traded_user_cnt:
            if hasattr(self.tapp_traded_user_cnt, 'to_alipay_dict'):
                params['tapp_traded_user_cnt'] = self.tapp_traded_user_cnt.to_alipay_dict()
            else:
                params['tapp_traded_user_cnt'] = self.tapp_traded_user_cnt
        if self.tapp_untraded_amt:
            if hasattr(self.tapp_untraded_amt, 'to_alipay_dict'):
                params['tapp_untraded_amt'] = self.tapp_untraded_amt.to_alipay_dict()
            else:
                params['tapp_untraded_amt'] = self.tapp_untraded_amt
        if self.tapp_untraded_cnt:
            if hasattr(self.tapp_untraded_cnt, 'to_alipay_dict'):
                params['tapp_untraded_cnt'] = self.tapp_untraded_cnt.to_alipay_dict()
            else:
                params['tapp_untraded_cnt'] = self.tapp_untraded_cnt
        if self.tapp_untraded_user_cnt:
            if hasattr(self.tapp_untraded_user_cnt, 'to_alipay_dict'):
                params['tapp_untraded_user_cnt'] = self.tapp_untraded_user_cnt.to_alipay_dict()
            else:
                params['tapp_untraded_user_cnt'] = self.tapp_untraded_user_cnt
        if self.tapp_uv:
            if hasattr(self.tapp_uv, 'to_alipay_dict'):
                params['tapp_uv'] = self.tapp_uv.to_alipay_dict()
            else:
                params['tapp_uv'] = self.tapp_uv
        if self.tapp_visit_add_user_cvr:
            if hasattr(self.tapp_visit_add_user_cvr, 'to_alipay_dict'):
                params['tapp_visit_add_user_cvr'] = self.tapp_visit_add_user_cvr.to_alipay_dict()
            else:
                params['tapp_visit_add_user_cvr'] = self.tapp_visit_add_user_cvr
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
        if self.tapp_visit_untraded_user_cvr:
            if hasattr(self.tapp_visit_untraded_user_cvr, 'to_alipay_dict'):
                params['tapp_visit_untraded_user_cvr'] = self.tapp_visit_untraded_user_cvr.to_alipay_dict()
            else:
                params['tapp_visit_untraded_user_cvr'] = self.tapp_visit_untraded_user_cvr
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiOperationAnalysisTrafficAliasDTO()
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
        if 'per_customer_price' in d:
            o.per_customer_price = d['per_customer_price']
        if 'per_unit_price' in d:
            o.per_unit_price = d['per_unit_price']
        if 'tapp_add_order_cnt' in d:
            o.tapp_add_order_cnt = d['tapp_add_order_cnt']
        if 'tapp_add_sku_cnt' in d:
            o.tapp_add_sku_cnt = d['tapp_add_sku_cnt']
        if 'tapp_add_user_cnt' in d:
            o.tapp_add_user_cnt = d['tapp_add_user_cnt']
        if 'tapp_new_uv' in d:
            o.tapp_new_uv = d['tapp_new_uv']
        if 'tapp_old_uv' in d:
            o.tapp_old_uv = d['tapp_old_uv']
        if 'tapp_order_amt' in d:
            o.tapp_order_amt = d['tapp_order_amt']
        if 'tapp_order_cnt' in d:
            o.tapp_order_cnt = d['tapp_order_cnt']
        if 'tapp_order_user_cnt' in d:
            o.tapp_order_user_cnt = d['tapp_order_user_cnt']
        if 'tapp_pv' in d:
            o.tapp_pv = d['tapp_pv']
        if 'tapp_refund_amt' in d:
            o.tapp_refund_amt = d['tapp_refund_amt']
        if 'tapp_refund_cnt' in d:
            o.tapp_refund_cnt = d['tapp_refund_cnt']
        if 'tapp_refund_user_cnt' in d:
            o.tapp_refund_user_cnt = d['tapp_refund_user_cnt']
        if 'tapp_traded_amt' in d:
            o.tapp_traded_amt = d['tapp_traded_amt']
        if 'tapp_traded_cnt' in d:
            o.tapp_traded_cnt = d['tapp_traded_cnt']
        if 'tapp_traded_refund_user_cvr' in d:
            o.tapp_traded_refund_user_cvr = d['tapp_traded_refund_user_cvr']
        if 'tapp_traded_user_cnt' in d:
            o.tapp_traded_user_cnt = d['tapp_traded_user_cnt']
        if 'tapp_untraded_amt' in d:
            o.tapp_untraded_amt = d['tapp_untraded_amt']
        if 'tapp_untraded_cnt' in d:
            o.tapp_untraded_cnt = d['tapp_untraded_cnt']
        if 'tapp_untraded_user_cnt' in d:
            o.tapp_untraded_user_cnt = d['tapp_untraded_user_cnt']
        if 'tapp_uv' in d:
            o.tapp_uv = d['tapp_uv']
        if 'tapp_visit_add_user_cvr' in d:
            o.tapp_visit_add_user_cvr = d['tapp_visit_add_user_cvr']
        if 'tapp_visit_order_user_cvr' in d:
            o.tapp_visit_order_user_cvr = d['tapp_visit_order_user_cvr']
        if 'tapp_visit_traded_user_cvr' in d:
            o.tapp_visit_traded_user_cvr = d['tapp_visit_traded_user_cvr']
        if 'tapp_visit_untraded_user_cvr' in d:
            o.tapp_visit_untraded_user_cvr = d['tapp_visit_untraded_user_cvr']
        return o


