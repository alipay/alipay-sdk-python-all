#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueBaseDTO import OperationValueBaseDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO
from alipay.aop.api.domain.OperationValueLongDTO import OperationValueLongDTO


class OpenApiOperationAnalysisTrafficPageAliasDTO(object):

    def __init__(self):
        self._alipay_app_id = None
        self._alipay_app_name = None
        self._channel_type = None
        self._dt = None
        self._end_page_user_cnt = None
        self._end_page_user_cnt_rate = None
        self._guid_add_order_user_cvr = None
        self._guid_add_user_cnt = None
        self._guid_order_user_cnt = None
        self._guid_share_cnt = None
        self._guid_share_user_cnt = None
        self._guid_visit_add_user_cvr = None
        self._multi_app_id = None
        self._multi_app_name = None
        self._page_name = None
        self._page_url = None
        self._pv = None
        self._stay_second_avg = None
        self._uv = None

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
    def end_page_user_cnt(self):
        return self._end_page_user_cnt

    @end_page_user_cnt.setter
    def end_page_user_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._end_page_user_cnt = value
        else:
            self._end_page_user_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def end_page_user_cnt_rate(self):
        return self._end_page_user_cnt_rate

    @end_page_user_cnt_rate.setter
    def end_page_user_cnt_rate(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._end_page_user_cnt_rate = value
        else:
            self._end_page_user_cnt_rate = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def guid_add_order_user_cvr(self):
        return self._guid_add_order_user_cvr

    @guid_add_order_user_cvr.setter
    def guid_add_order_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._guid_add_order_user_cvr = value
        else:
            self._guid_add_order_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)
    @property
    def guid_add_user_cnt(self):
        return self._guid_add_user_cnt

    @guid_add_user_cnt.setter
    def guid_add_user_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._guid_add_user_cnt = value
        else:
            self._guid_add_user_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def guid_order_user_cnt(self):
        return self._guid_order_user_cnt

    @guid_order_user_cnt.setter
    def guid_order_user_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._guid_order_user_cnt = value
        else:
            self._guid_order_user_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def guid_share_cnt(self):
        return self._guid_share_cnt

    @guid_share_cnt.setter
    def guid_share_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._guid_share_cnt = value
        else:
            self._guid_share_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def guid_share_user_cnt(self):
        return self._guid_share_user_cnt

    @guid_share_user_cnt.setter
    def guid_share_user_cnt(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._guid_share_user_cnt = value
        else:
            self._guid_share_user_cnt = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def guid_visit_add_user_cvr(self):
        return self._guid_visit_add_user_cvr

    @guid_visit_add_user_cvr.setter
    def guid_visit_add_user_cvr(self, value):
        if isinstance(value, OperationValueBaseDTO):
            self._guid_visit_add_user_cvr = value
        else:
            self._guid_visit_add_user_cvr = OperationValueBaseDTO.from_alipay_dict(value)
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
    def page_name(self):
        return self._page_name

    @page_name.setter
    def page_name(self, value):
        self._page_name = value
    @property
    def page_url(self):
        return self._page_url

    @page_url.setter
    def page_url(self, value):
        self._page_url = value
    @property
    def pv(self):
        return self._pv

    @pv.setter
    def pv(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._pv = value
        else:
            self._pv = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def stay_second_avg(self):
        return self._stay_second_avg

    @stay_second_avg.setter
    def stay_second_avg(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._stay_second_avg = value
        else:
            self._stay_second_avg = OperationValueLongDTO.from_alipay_dict(value)
    @property
    def uv(self):
        return self._uv

    @uv.setter
    def uv(self, value):
        if isinstance(value, OperationValueLongDTO):
            self._uv = value
        else:
            self._uv = OperationValueLongDTO.from_alipay_dict(value)


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
        if self.end_page_user_cnt:
            if hasattr(self.end_page_user_cnt, 'to_alipay_dict'):
                params['end_page_user_cnt'] = self.end_page_user_cnt.to_alipay_dict()
            else:
                params['end_page_user_cnt'] = self.end_page_user_cnt
        if self.end_page_user_cnt_rate:
            if hasattr(self.end_page_user_cnt_rate, 'to_alipay_dict'):
                params['end_page_user_cnt_rate'] = self.end_page_user_cnt_rate.to_alipay_dict()
            else:
                params['end_page_user_cnt_rate'] = self.end_page_user_cnt_rate
        if self.guid_add_order_user_cvr:
            if hasattr(self.guid_add_order_user_cvr, 'to_alipay_dict'):
                params['guid_add_order_user_cvr'] = self.guid_add_order_user_cvr.to_alipay_dict()
            else:
                params['guid_add_order_user_cvr'] = self.guid_add_order_user_cvr
        if self.guid_add_user_cnt:
            if hasattr(self.guid_add_user_cnt, 'to_alipay_dict'):
                params['guid_add_user_cnt'] = self.guid_add_user_cnt.to_alipay_dict()
            else:
                params['guid_add_user_cnt'] = self.guid_add_user_cnt
        if self.guid_order_user_cnt:
            if hasattr(self.guid_order_user_cnt, 'to_alipay_dict'):
                params['guid_order_user_cnt'] = self.guid_order_user_cnt.to_alipay_dict()
            else:
                params['guid_order_user_cnt'] = self.guid_order_user_cnt
        if self.guid_share_cnt:
            if hasattr(self.guid_share_cnt, 'to_alipay_dict'):
                params['guid_share_cnt'] = self.guid_share_cnt.to_alipay_dict()
            else:
                params['guid_share_cnt'] = self.guid_share_cnt
        if self.guid_share_user_cnt:
            if hasattr(self.guid_share_user_cnt, 'to_alipay_dict'):
                params['guid_share_user_cnt'] = self.guid_share_user_cnt.to_alipay_dict()
            else:
                params['guid_share_user_cnt'] = self.guid_share_user_cnt
        if self.guid_visit_add_user_cvr:
            if hasattr(self.guid_visit_add_user_cvr, 'to_alipay_dict'):
                params['guid_visit_add_user_cvr'] = self.guid_visit_add_user_cvr.to_alipay_dict()
            else:
                params['guid_visit_add_user_cvr'] = self.guid_visit_add_user_cvr
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
        if self.page_name:
            if hasattr(self.page_name, 'to_alipay_dict'):
                params['page_name'] = self.page_name.to_alipay_dict()
            else:
                params['page_name'] = self.page_name
        if self.page_url:
            if hasattr(self.page_url, 'to_alipay_dict'):
                params['page_url'] = self.page_url.to_alipay_dict()
            else:
                params['page_url'] = self.page_url
        if self.pv:
            if hasattr(self.pv, 'to_alipay_dict'):
                params['pv'] = self.pv.to_alipay_dict()
            else:
                params['pv'] = self.pv
        if self.stay_second_avg:
            if hasattr(self.stay_second_avg, 'to_alipay_dict'):
                params['stay_second_avg'] = self.stay_second_avg.to_alipay_dict()
            else:
                params['stay_second_avg'] = self.stay_second_avg
        if self.uv:
            if hasattr(self.uv, 'to_alipay_dict'):
                params['uv'] = self.uv.to_alipay_dict()
            else:
                params['uv'] = self.uv
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiOperationAnalysisTrafficPageAliasDTO()
        if 'alipay_app_id' in d:
            o.alipay_app_id = d['alipay_app_id']
        if 'alipay_app_name' in d:
            o.alipay_app_name = d['alipay_app_name']
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'dt' in d:
            o.dt = d['dt']
        if 'end_page_user_cnt' in d:
            o.end_page_user_cnt = d['end_page_user_cnt']
        if 'end_page_user_cnt_rate' in d:
            o.end_page_user_cnt_rate = d['end_page_user_cnt_rate']
        if 'guid_add_order_user_cvr' in d:
            o.guid_add_order_user_cvr = d['guid_add_order_user_cvr']
        if 'guid_add_user_cnt' in d:
            o.guid_add_user_cnt = d['guid_add_user_cnt']
        if 'guid_order_user_cnt' in d:
            o.guid_order_user_cnt = d['guid_order_user_cnt']
        if 'guid_share_cnt' in d:
            o.guid_share_cnt = d['guid_share_cnt']
        if 'guid_share_user_cnt' in d:
            o.guid_share_user_cnt = d['guid_share_user_cnt']
        if 'guid_visit_add_user_cvr' in d:
            o.guid_visit_add_user_cvr = d['guid_visit_add_user_cvr']
        if 'multi_app_id' in d:
            o.multi_app_id = d['multi_app_id']
        if 'multi_app_name' in d:
            o.multi_app_name = d['multi_app_name']
        if 'page_name' in d:
            o.page_name = d['page_name']
        if 'page_url' in d:
            o.page_url = d['page_url']
        if 'pv' in d:
            o.pv = d['pv']
        if 'stay_second_avg' in d:
            o.stay_second_avg = d['stay_second_avg']
        if 'uv' in d:
            o.uv = d['uv']
        return o


