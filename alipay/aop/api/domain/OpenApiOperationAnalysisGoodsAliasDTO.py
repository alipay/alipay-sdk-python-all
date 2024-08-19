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
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO


class OpenApiOperationAnalysisGoodsAliasDTO(object):

    def __init__(self):
        self._alipay_app_id = None
        self._alipay_app_name = None
        self._channel_type = None
        self._dt = None
        self._multi_app_id = None
        self._multi_app_name = None
        self._per_customer_price = None
        self._per_unit_price = None
        self._spu_add_order_cnt = None
        self._spu_add_sku_cnt = None
        self._spu_add_user_cnt = None
        self._spu_expo_pv = None
        self._spu_month_repurchase_rate = None
        self._spu_order_amt = None
        self._spu_order_cnt = None
        self._spu_order_user_cnt = None
        self._spu_refund_amt = None
        self._spu_refund_cnt = None
        self._spu_refund_user_cnt = None
        self._spu_season_repurchase_rate = None
        self._spu_traded_amt = None
        self._spu_traded_cnt = None
        self._spu_traded_refund_user_cvr = None
        self._spu_traded_user_cnt = None
        self._spu_untraded_amt = None
        self._spu_untraded_cnt = None
        self._spu_untraded_user_cnt = None
        self._spu_uv = None
        self._spu_visit_add_user_cvr = None
        self._spu_visit_cnt = None
        self._spu_visit_order_user_cvr = None
        self._spu_visit_traded_user_cvr = None
        self._spu_visit_untrade_user_cvr = None

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
    def spu_add_order_cnt(self):
        return self._spu_add_order_cnt

    @spu_add_order_cnt.setter
    def spu_add_order_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._spu_add_order_cnt = value
        else:
            self._spu_add_order_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def spu_add_sku_cnt(self):
        return self._spu_add_sku_cnt

    @spu_add_sku_cnt.setter
    def spu_add_sku_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._spu_add_sku_cnt = value
        else:
            self._spu_add_sku_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def spu_add_user_cnt(self):
        return self._spu_add_user_cnt

    @spu_add_user_cnt.setter
    def spu_add_user_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._spu_add_user_cnt = value
        else:
            self._spu_add_user_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def spu_expo_pv(self):
        return self._spu_expo_pv

    @spu_expo_pv.setter
    def spu_expo_pv(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._spu_expo_pv = value
        else:
            self._spu_expo_pv = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def spu_month_repurchase_rate(self):
        return self._spu_month_repurchase_rate

    @spu_month_repurchase_rate.setter
    def spu_month_repurchase_rate(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._spu_month_repurchase_rate = value
        else:
            self._spu_month_repurchase_rate = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def spu_order_amt(self):
        return self._spu_order_amt

    @spu_order_amt.setter
    def spu_order_amt(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._spu_order_amt = value
        else:
            self._spu_order_amt = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def spu_order_cnt(self):
        return self._spu_order_cnt

    @spu_order_cnt.setter
    def spu_order_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._spu_order_cnt = value
        else:
            self._spu_order_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def spu_order_user_cnt(self):
        return self._spu_order_user_cnt

    @spu_order_user_cnt.setter
    def spu_order_user_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._spu_order_user_cnt = value
        else:
            self._spu_order_user_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def spu_refund_amt(self):
        return self._spu_refund_amt

    @spu_refund_amt.setter
    def spu_refund_amt(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._spu_refund_amt = value
        else:
            self._spu_refund_amt = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def spu_refund_cnt(self):
        return self._spu_refund_cnt

    @spu_refund_cnt.setter
    def spu_refund_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._spu_refund_cnt = value
        else:
            self._spu_refund_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def spu_refund_user_cnt(self):
        return self._spu_refund_user_cnt

    @spu_refund_user_cnt.setter
    def spu_refund_user_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._spu_refund_user_cnt = value
        else:
            self._spu_refund_user_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def spu_season_repurchase_rate(self):
        return self._spu_season_repurchase_rate

    @spu_season_repurchase_rate.setter
    def spu_season_repurchase_rate(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._spu_season_repurchase_rate = value
        else:
            self._spu_season_repurchase_rate = OperationValueBaseDTO.from_alipay_dict(value)
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
    def spu_traded_cnt(self):
        return self._spu_traded_cnt

    @spu_traded_cnt.setter
    def spu_traded_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._spu_traded_cnt = value
        else:
            self._spu_traded_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def spu_traded_refund_user_cvr(self):
        return self._spu_traded_refund_user_cvr

    @spu_traded_refund_user_cvr.setter
    def spu_traded_refund_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._spu_traded_refund_user_cvr = value
        else:
            self._spu_traded_refund_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def spu_traded_user_cnt(self):
        return self._spu_traded_user_cnt

    @spu_traded_user_cnt.setter
    def spu_traded_user_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._spu_traded_user_cnt = value
        else:
            self._spu_traded_user_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def spu_untraded_amt(self):
        return self._spu_untraded_amt

    @spu_untraded_amt.setter
    def spu_untraded_amt(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._spu_untraded_amt = value
        else:
            self._spu_untraded_amt = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def spu_untraded_cnt(self):
        return self._spu_untraded_cnt

    @spu_untraded_cnt.setter
    def spu_untraded_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._spu_untraded_cnt = value
        else:
            self._spu_untraded_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def spu_untraded_user_cnt(self):
        return self._spu_untraded_user_cnt

    @spu_untraded_user_cnt.setter
    def spu_untraded_user_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._spu_untraded_user_cnt = value
        else:
            self._spu_untraded_user_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def spu_uv(self):
        return self._spu_uv

    @spu_uv.setter
    def spu_uv(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._spu_uv = value
        else:
            self._spu_uv = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def spu_visit_add_user_cvr(self):
        return self._spu_visit_add_user_cvr

    @spu_visit_add_user_cvr.setter
    def spu_visit_add_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._spu_visit_add_user_cvr = value
        else:
            self._spu_visit_add_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def spu_visit_cnt(self):
        return self._spu_visit_cnt

    @spu_visit_cnt.setter
    def spu_visit_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._spu_visit_cnt = value
        else:
            self._spu_visit_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def spu_visit_order_user_cvr(self):
        return self._spu_visit_order_user_cvr

    @spu_visit_order_user_cvr.setter
    def spu_visit_order_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._spu_visit_order_user_cvr = value
        else:
            self._spu_visit_order_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def spu_visit_traded_user_cvr(self):
        return self._spu_visit_traded_user_cvr

    @spu_visit_traded_user_cvr.setter
    def spu_visit_traded_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._spu_visit_traded_user_cvr = value
        else:
            self._spu_visit_traded_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def spu_visit_untrade_user_cvr(self):
        return self._spu_visit_untrade_user_cvr

    @spu_visit_untrade_user_cvr.setter
    def spu_visit_untrade_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._spu_visit_untrade_user_cvr = value
        else:
            self._spu_visit_untrade_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)


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
        if self.spu_add_order_cnt:
            if hasattr(self.spu_add_order_cnt, 'to_alipay_dict'):
                params['spu_add_order_cnt'] = self.spu_add_order_cnt.to_alipay_dict()
            else:
                params['spu_add_order_cnt'] = self.spu_add_order_cnt
        if self.spu_add_sku_cnt:
            if hasattr(self.spu_add_sku_cnt, 'to_alipay_dict'):
                params['spu_add_sku_cnt'] = self.spu_add_sku_cnt.to_alipay_dict()
            else:
                params['spu_add_sku_cnt'] = self.spu_add_sku_cnt
        if self.spu_add_user_cnt:
            if hasattr(self.spu_add_user_cnt, 'to_alipay_dict'):
                params['spu_add_user_cnt'] = self.spu_add_user_cnt.to_alipay_dict()
            else:
                params['spu_add_user_cnt'] = self.spu_add_user_cnt
        if self.spu_expo_pv:
            if hasattr(self.spu_expo_pv, 'to_alipay_dict'):
                params['spu_expo_pv'] = self.spu_expo_pv.to_alipay_dict()
            else:
                params['spu_expo_pv'] = self.spu_expo_pv
        if self.spu_month_repurchase_rate:
            if hasattr(self.spu_month_repurchase_rate, 'to_alipay_dict'):
                params['spu_month_repurchase_rate'] = self.spu_month_repurchase_rate.to_alipay_dict()
            else:
                params['spu_month_repurchase_rate'] = self.spu_month_repurchase_rate
        if self.spu_order_amt:
            if hasattr(self.spu_order_amt, 'to_alipay_dict'):
                params['spu_order_amt'] = self.spu_order_amt.to_alipay_dict()
            else:
                params['spu_order_amt'] = self.spu_order_amt
        if self.spu_order_cnt:
            if hasattr(self.spu_order_cnt, 'to_alipay_dict'):
                params['spu_order_cnt'] = self.spu_order_cnt.to_alipay_dict()
            else:
                params['spu_order_cnt'] = self.spu_order_cnt
        if self.spu_order_user_cnt:
            if hasattr(self.spu_order_user_cnt, 'to_alipay_dict'):
                params['spu_order_user_cnt'] = self.spu_order_user_cnt.to_alipay_dict()
            else:
                params['spu_order_user_cnt'] = self.spu_order_user_cnt
        if self.spu_refund_amt:
            if hasattr(self.spu_refund_amt, 'to_alipay_dict'):
                params['spu_refund_amt'] = self.spu_refund_amt.to_alipay_dict()
            else:
                params['spu_refund_amt'] = self.spu_refund_amt
        if self.spu_refund_cnt:
            if hasattr(self.spu_refund_cnt, 'to_alipay_dict'):
                params['spu_refund_cnt'] = self.spu_refund_cnt.to_alipay_dict()
            else:
                params['spu_refund_cnt'] = self.spu_refund_cnt
        if self.spu_refund_user_cnt:
            if hasattr(self.spu_refund_user_cnt, 'to_alipay_dict'):
                params['spu_refund_user_cnt'] = self.spu_refund_user_cnt.to_alipay_dict()
            else:
                params['spu_refund_user_cnt'] = self.spu_refund_user_cnt
        if self.spu_season_repurchase_rate:
            if hasattr(self.spu_season_repurchase_rate, 'to_alipay_dict'):
                params['spu_season_repurchase_rate'] = self.spu_season_repurchase_rate.to_alipay_dict()
            else:
                params['spu_season_repurchase_rate'] = self.spu_season_repurchase_rate
        if self.spu_traded_amt:
            if hasattr(self.spu_traded_amt, 'to_alipay_dict'):
                params['spu_traded_amt'] = self.spu_traded_amt.to_alipay_dict()
            else:
                params['spu_traded_amt'] = self.spu_traded_amt
        if self.spu_traded_cnt:
            if hasattr(self.spu_traded_cnt, 'to_alipay_dict'):
                params['spu_traded_cnt'] = self.spu_traded_cnt.to_alipay_dict()
            else:
                params['spu_traded_cnt'] = self.spu_traded_cnt
        if self.spu_traded_refund_user_cvr:
            if hasattr(self.spu_traded_refund_user_cvr, 'to_alipay_dict'):
                params['spu_traded_refund_user_cvr'] = self.spu_traded_refund_user_cvr.to_alipay_dict()
            else:
                params['spu_traded_refund_user_cvr'] = self.spu_traded_refund_user_cvr
        if self.spu_traded_user_cnt:
            if hasattr(self.spu_traded_user_cnt, 'to_alipay_dict'):
                params['spu_traded_user_cnt'] = self.spu_traded_user_cnt.to_alipay_dict()
            else:
                params['spu_traded_user_cnt'] = self.spu_traded_user_cnt
        if self.spu_untraded_amt:
            if hasattr(self.spu_untraded_amt, 'to_alipay_dict'):
                params['spu_untraded_amt'] = self.spu_untraded_amt.to_alipay_dict()
            else:
                params['spu_untraded_amt'] = self.spu_untraded_amt
        if self.spu_untraded_cnt:
            if hasattr(self.spu_untraded_cnt, 'to_alipay_dict'):
                params['spu_untraded_cnt'] = self.spu_untraded_cnt.to_alipay_dict()
            else:
                params['spu_untraded_cnt'] = self.spu_untraded_cnt
        if self.spu_untraded_user_cnt:
            if hasattr(self.spu_untraded_user_cnt, 'to_alipay_dict'):
                params['spu_untraded_user_cnt'] = self.spu_untraded_user_cnt.to_alipay_dict()
            else:
                params['spu_untraded_user_cnt'] = self.spu_untraded_user_cnt
        if self.spu_uv:
            if hasattr(self.spu_uv, 'to_alipay_dict'):
                params['spu_uv'] = self.spu_uv.to_alipay_dict()
            else:
                params['spu_uv'] = self.spu_uv
        if self.spu_visit_add_user_cvr:
            if hasattr(self.spu_visit_add_user_cvr, 'to_alipay_dict'):
                params['spu_visit_add_user_cvr'] = self.spu_visit_add_user_cvr.to_alipay_dict()
            else:
                params['spu_visit_add_user_cvr'] = self.spu_visit_add_user_cvr
        if self.spu_visit_cnt:
            if hasattr(self.spu_visit_cnt, 'to_alipay_dict'):
                params['spu_visit_cnt'] = self.spu_visit_cnt.to_alipay_dict()
            else:
                params['spu_visit_cnt'] = self.spu_visit_cnt
        if self.spu_visit_order_user_cvr:
            if hasattr(self.spu_visit_order_user_cvr, 'to_alipay_dict'):
                params['spu_visit_order_user_cvr'] = self.spu_visit_order_user_cvr.to_alipay_dict()
            else:
                params['spu_visit_order_user_cvr'] = self.spu_visit_order_user_cvr
        if self.spu_visit_traded_user_cvr:
            if hasattr(self.spu_visit_traded_user_cvr, 'to_alipay_dict'):
                params['spu_visit_traded_user_cvr'] = self.spu_visit_traded_user_cvr.to_alipay_dict()
            else:
                params['spu_visit_traded_user_cvr'] = self.spu_visit_traded_user_cvr
        if self.spu_visit_untrade_user_cvr:
            if hasattr(self.spu_visit_untrade_user_cvr, 'to_alipay_dict'):
                params['spu_visit_untrade_user_cvr'] = self.spu_visit_untrade_user_cvr.to_alipay_dict()
            else:
                params['spu_visit_untrade_user_cvr'] = self.spu_visit_untrade_user_cvr
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiOperationAnalysisGoodsAliasDTO()
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
        if 'spu_add_order_cnt' in d:
            o.spu_add_order_cnt = d['spu_add_order_cnt']
        if 'spu_add_sku_cnt' in d:
            o.spu_add_sku_cnt = d['spu_add_sku_cnt']
        if 'spu_add_user_cnt' in d:
            o.spu_add_user_cnt = d['spu_add_user_cnt']
        if 'spu_expo_pv' in d:
            o.spu_expo_pv = d['spu_expo_pv']
        if 'spu_month_repurchase_rate' in d:
            o.spu_month_repurchase_rate = d['spu_month_repurchase_rate']
        if 'spu_order_amt' in d:
            o.spu_order_amt = d['spu_order_amt']
        if 'spu_order_cnt' in d:
            o.spu_order_cnt = d['spu_order_cnt']
        if 'spu_order_user_cnt' in d:
            o.spu_order_user_cnt = d['spu_order_user_cnt']
        if 'spu_refund_amt' in d:
            o.spu_refund_amt = d['spu_refund_amt']
        if 'spu_refund_cnt' in d:
            o.spu_refund_cnt = d['spu_refund_cnt']
        if 'spu_refund_user_cnt' in d:
            o.spu_refund_user_cnt = d['spu_refund_user_cnt']
        if 'spu_season_repurchase_rate' in d:
            o.spu_season_repurchase_rate = d['spu_season_repurchase_rate']
        if 'spu_traded_amt' in d:
            o.spu_traded_amt = d['spu_traded_amt']
        if 'spu_traded_cnt' in d:
            o.spu_traded_cnt = d['spu_traded_cnt']
        if 'spu_traded_refund_user_cvr' in d:
            o.spu_traded_refund_user_cvr = d['spu_traded_refund_user_cvr']
        if 'spu_traded_user_cnt' in d:
            o.spu_traded_user_cnt = d['spu_traded_user_cnt']
        if 'spu_untraded_amt' in d:
            o.spu_untraded_amt = d['spu_untraded_amt']
        if 'spu_untraded_cnt' in d:
            o.spu_untraded_cnt = d['spu_untraded_cnt']
        if 'spu_untraded_user_cnt' in d:
            o.spu_untraded_user_cnt = d['spu_untraded_user_cnt']
        if 'spu_uv' in d:
            o.spu_uv = d['spu_uv']
        if 'spu_visit_add_user_cvr' in d:
            o.spu_visit_add_user_cvr = d['spu_visit_add_user_cvr']
        if 'spu_visit_cnt' in d:
            o.spu_visit_cnt = d['spu_visit_cnt']
        if 'spu_visit_order_user_cvr' in d:
            o.spu_visit_order_user_cvr = d['spu_visit_order_user_cvr']
        if 'spu_visit_traded_user_cvr' in d:
            o.spu_visit_traded_user_cvr = d['spu_visit_traded_user_cvr']
        if 'spu_visit_untrade_user_cvr' in d:
            o.spu_visit_untrade_user_cvr = d['spu_visit_untrade_user_cvr']
        return o


