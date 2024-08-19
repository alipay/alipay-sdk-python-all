#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO


class OpenApiOperationAnalysisCategoryDetailAliasDTO(object):

    def __init__(self):
        self._alipay_app_id = None
        self._alipay_app_name = None
        self._cate_add_user_cnt = None
        self._cate_expo_pv = None
        self._cate_id = None
        self._cate_month_repurchase_rate = None
        self._cate_name = None
        self._cate_order_traded_user_cvr = None
        self._cate_order_user_cnt = None
        self._cate_pv_share_rate = None
        self._cate_season_repurchase_rate = None
        self._cate_traded_amt = None
        self._cate_traded_sales_cnt = None
        self._cate_traded_share_rate = None
        self._cate_traded_user_cnt = None
        self._cate_uv = None
        self._cate_visit_order_user_cvr = None
        self._cate_visit_traded_user_cvr = None
        self._channel_type = None
        self._dt = None
        self._multi_app_id = None
        self._multi_app_name = None

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
    def cate_add_user_cnt(self):
        return self._cate_add_user_cnt

    @cate_add_user_cnt.setter
    def cate_add_user_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._cate_add_user_cnt = value
        else:
            self._cate_add_user_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def cate_expo_pv(self):
        return self._cate_expo_pv

    @cate_expo_pv.setter
    def cate_expo_pv(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._cate_expo_pv = value
        else:
            self._cate_expo_pv = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def cate_id(self):
        return self._cate_id

    @cate_id.setter
    def cate_id(self, value):
        self._cate_id = value
    @property
    def cate_month_repurchase_rate(self):
        return self._cate_month_repurchase_rate

    @cate_month_repurchase_rate.setter
    def cate_month_repurchase_rate(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._cate_month_repurchase_rate = value
        else:
            self._cate_month_repurchase_rate = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def cate_name(self):
        return self._cate_name

    @cate_name.setter
    def cate_name(self, value):
        self._cate_name = value
    @property
    def cate_order_traded_user_cvr(self):
        return self._cate_order_traded_user_cvr

    @cate_order_traded_user_cvr.setter
    def cate_order_traded_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._cate_order_traded_user_cvr = value
        else:
            self._cate_order_traded_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def cate_order_user_cnt(self):
        return self._cate_order_user_cnt

    @cate_order_user_cnt.setter
    def cate_order_user_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._cate_order_user_cnt = value
        else:
            self._cate_order_user_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def cate_pv_share_rate(self):
        return self._cate_pv_share_rate

    @cate_pv_share_rate.setter
    def cate_pv_share_rate(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._cate_pv_share_rate = value
        else:
            self._cate_pv_share_rate = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def cate_season_repurchase_rate(self):
        return self._cate_season_repurchase_rate

    @cate_season_repurchase_rate.setter
    def cate_season_repurchase_rate(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._cate_season_repurchase_rate = value
        else:
            self._cate_season_repurchase_rate = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def cate_traded_amt(self):
        return self._cate_traded_amt

    @cate_traded_amt.setter
    def cate_traded_amt(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._cate_traded_amt = value
        else:
            self._cate_traded_amt = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def cate_traded_sales_cnt(self):
        return self._cate_traded_sales_cnt

    @cate_traded_sales_cnt.setter
    def cate_traded_sales_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._cate_traded_sales_cnt = value
        else:
            self._cate_traded_sales_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def cate_traded_share_rate(self):
        return self._cate_traded_share_rate

    @cate_traded_share_rate.setter
    def cate_traded_share_rate(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._cate_traded_share_rate = value
        else:
            self._cate_traded_share_rate = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def cate_traded_user_cnt(self):
        return self._cate_traded_user_cnt

    @cate_traded_user_cnt.setter
    def cate_traded_user_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._cate_traded_user_cnt = value
        else:
            self._cate_traded_user_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def cate_uv(self):
        return self._cate_uv

    @cate_uv.setter
    def cate_uv(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._cate_uv = value
        else:
            self._cate_uv = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def cate_visit_order_user_cvr(self):
        return self._cate_visit_order_user_cvr

    @cate_visit_order_user_cvr.setter
    def cate_visit_order_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._cate_visit_order_user_cvr = value
        else:
            self._cate_visit_order_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def cate_visit_traded_user_cvr(self):
        return self._cate_visit_traded_user_cvr

    @cate_visit_traded_user_cvr.setter
    def cate_visit_traded_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._cate_visit_traded_user_cvr = value
        else:
            self._cate_visit_traded_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)
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
        if self.cate_add_user_cnt:
            if hasattr(self.cate_add_user_cnt, 'to_alipay_dict'):
                params['cate_add_user_cnt'] = self.cate_add_user_cnt.to_alipay_dict()
            else:
                params['cate_add_user_cnt'] = self.cate_add_user_cnt
        if self.cate_expo_pv:
            if hasattr(self.cate_expo_pv, 'to_alipay_dict'):
                params['cate_expo_pv'] = self.cate_expo_pv.to_alipay_dict()
            else:
                params['cate_expo_pv'] = self.cate_expo_pv
        if self.cate_id:
            if hasattr(self.cate_id, 'to_alipay_dict'):
                params['cate_id'] = self.cate_id.to_alipay_dict()
            else:
                params['cate_id'] = self.cate_id
        if self.cate_month_repurchase_rate:
            if hasattr(self.cate_month_repurchase_rate, 'to_alipay_dict'):
                params['cate_month_repurchase_rate'] = self.cate_month_repurchase_rate.to_alipay_dict()
            else:
                params['cate_month_repurchase_rate'] = self.cate_month_repurchase_rate
        if self.cate_name:
            if hasattr(self.cate_name, 'to_alipay_dict'):
                params['cate_name'] = self.cate_name.to_alipay_dict()
            else:
                params['cate_name'] = self.cate_name
        if self.cate_order_traded_user_cvr:
            if hasattr(self.cate_order_traded_user_cvr, 'to_alipay_dict'):
                params['cate_order_traded_user_cvr'] = self.cate_order_traded_user_cvr.to_alipay_dict()
            else:
                params['cate_order_traded_user_cvr'] = self.cate_order_traded_user_cvr
        if self.cate_order_user_cnt:
            if hasattr(self.cate_order_user_cnt, 'to_alipay_dict'):
                params['cate_order_user_cnt'] = self.cate_order_user_cnt.to_alipay_dict()
            else:
                params['cate_order_user_cnt'] = self.cate_order_user_cnt
        if self.cate_pv_share_rate:
            if hasattr(self.cate_pv_share_rate, 'to_alipay_dict'):
                params['cate_pv_share_rate'] = self.cate_pv_share_rate.to_alipay_dict()
            else:
                params['cate_pv_share_rate'] = self.cate_pv_share_rate
        if self.cate_season_repurchase_rate:
            if hasattr(self.cate_season_repurchase_rate, 'to_alipay_dict'):
                params['cate_season_repurchase_rate'] = self.cate_season_repurchase_rate.to_alipay_dict()
            else:
                params['cate_season_repurchase_rate'] = self.cate_season_repurchase_rate
        if self.cate_traded_amt:
            if hasattr(self.cate_traded_amt, 'to_alipay_dict'):
                params['cate_traded_amt'] = self.cate_traded_amt.to_alipay_dict()
            else:
                params['cate_traded_amt'] = self.cate_traded_amt
        if self.cate_traded_sales_cnt:
            if hasattr(self.cate_traded_sales_cnt, 'to_alipay_dict'):
                params['cate_traded_sales_cnt'] = self.cate_traded_sales_cnt.to_alipay_dict()
            else:
                params['cate_traded_sales_cnt'] = self.cate_traded_sales_cnt
        if self.cate_traded_share_rate:
            if hasattr(self.cate_traded_share_rate, 'to_alipay_dict'):
                params['cate_traded_share_rate'] = self.cate_traded_share_rate.to_alipay_dict()
            else:
                params['cate_traded_share_rate'] = self.cate_traded_share_rate
        if self.cate_traded_user_cnt:
            if hasattr(self.cate_traded_user_cnt, 'to_alipay_dict'):
                params['cate_traded_user_cnt'] = self.cate_traded_user_cnt.to_alipay_dict()
            else:
                params['cate_traded_user_cnt'] = self.cate_traded_user_cnt
        if self.cate_uv:
            if hasattr(self.cate_uv, 'to_alipay_dict'):
                params['cate_uv'] = self.cate_uv.to_alipay_dict()
            else:
                params['cate_uv'] = self.cate_uv
        if self.cate_visit_order_user_cvr:
            if hasattr(self.cate_visit_order_user_cvr, 'to_alipay_dict'):
                params['cate_visit_order_user_cvr'] = self.cate_visit_order_user_cvr.to_alipay_dict()
            else:
                params['cate_visit_order_user_cvr'] = self.cate_visit_order_user_cvr
        if self.cate_visit_traded_user_cvr:
            if hasattr(self.cate_visit_traded_user_cvr, 'to_alipay_dict'):
                params['cate_visit_traded_user_cvr'] = self.cate_visit_traded_user_cvr.to_alipay_dict()
            else:
                params['cate_visit_traded_user_cvr'] = self.cate_visit_traded_user_cvr
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiOperationAnalysisCategoryDetailAliasDTO()
        if 'alipay_app_id' in d:
            o.alipay_app_id = d['alipay_app_id']
        if 'alipay_app_name' in d:
            o.alipay_app_name = d['alipay_app_name']
        if 'cate_add_user_cnt' in d:
            o.cate_add_user_cnt = d['cate_add_user_cnt']
        if 'cate_expo_pv' in d:
            o.cate_expo_pv = d['cate_expo_pv']
        if 'cate_id' in d:
            o.cate_id = d['cate_id']
        if 'cate_month_repurchase_rate' in d:
            o.cate_month_repurchase_rate = d['cate_month_repurchase_rate']
        if 'cate_name' in d:
            o.cate_name = d['cate_name']
        if 'cate_order_traded_user_cvr' in d:
            o.cate_order_traded_user_cvr = d['cate_order_traded_user_cvr']
        if 'cate_order_user_cnt' in d:
            o.cate_order_user_cnt = d['cate_order_user_cnt']
        if 'cate_pv_share_rate' in d:
            o.cate_pv_share_rate = d['cate_pv_share_rate']
        if 'cate_season_repurchase_rate' in d:
            o.cate_season_repurchase_rate = d['cate_season_repurchase_rate']
        if 'cate_traded_amt' in d:
            o.cate_traded_amt = d['cate_traded_amt']
        if 'cate_traded_sales_cnt' in d:
            o.cate_traded_sales_cnt = d['cate_traded_sales_cnt']
        if 'cate_traded_share_rate' in d:
            o.cate_traded_share_rate = d['cate_traded_share_rate']
        if 'cate_traded_user_cnt' in d:
            o.cate_traded_user_cnt = d['cate_traded_user_cnt']
        if 'cate_uv' in d:
            o.cate_uv = d['cate_uv']
        if 'cate_visit_order_user_cvr' in d:
            o.cate_visit_order_user_cvr = d['cate_visit_order_user_cvr']
        if 'cate_visit_traded_user_cvr' in d:
            o.cate_visit_traded_user_cvr = d['cate_visit_traded_user_cvr']
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'dt' in d:
            o.dt = d['dt']
        if 'multi_app_id' in d:
            o.multi_app_id = d['multi_app_id']
        if 'multi_app_name' in d:
            o.multi_app_name = d['multi_app_name']
        return o


