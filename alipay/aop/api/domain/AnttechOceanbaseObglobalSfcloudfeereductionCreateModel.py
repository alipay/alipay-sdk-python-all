#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SaleForceCompetitorDTO import SaleForceCompetitorDTO


class AnttechOceanbaseObglobalSfcloudfeereductionCreateModel(object):

    def __init__(self):
        self._apply_reason = None
        self._bd_work_no = None
        self._comment = None
        self._competitor_list = None
        self._coupon_end_time = None
        self._coupon_name = None
        self._coupon_start_time = None
        self._coupon_validity_type = None
        self._cumulative_arr = None
        self._denomination = None
        self._leads_code = None
        self._ob_passport_id = None
        self._pain_spot_list = None
        self._reduction_reason = None
        self._region = None
        self._sales_force_id = None
        self._third_party_passport_id = None
        self._time_value = None

    @property
    def apply_reason(self):
        return self._apply_reason

    @apply_reason.setter
    def apply_reason(self, value):
        self._apply_reason = value
    @property
    def bd_work_no(self):
        return self._bd_work_no

    @bd_work_no.setter
    def bd_work_no(self, value):
        self._bd_work_no = value
    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
    @property
    def competitor_list(self):
        return self._competitor_list

    @competitor_list.setter
    def competitor_list(self, value):
        if isinstance(value, list):
            self._competitor_list = list()
            for i in value:
                if isinstance(i, SaleForceCompetitorDTO):
                    self._competitor_list.append(i)
                else:
                    self._competitor_list.append(SaleForceCompetitorDTO.from_alipay_dict(i))
    @property
    def coupon_end_time(self):
        return self._coupon_end_time

    @coupon_end_time.setter
    def coupon_end_time(self, value):
        self._coupon_end_time = value
    @property
    def coupon_name(self):
        return self._coupon_name

    @coupon_name.setter
    def coupon_name(self, value):
        self._coupon_name = value
    @property
    def coupon_start_time(self):
        return self._coupon_start_time

    @coupon_start_time.setter
    def coupon_start_time(self, value):
        self._coupon_start_time = value
    @property
    def coupon_validity_type(self):
        return self._coupon_validity_type

    @coupon_validity_type.setter
    def coupon_validity_type(self, value):
        self._coupon_validity_type = value
    @property
    def cumulative_arr(self):
        return self._cumulative_arr

    @cumulative_arr.setter
    def cumulative_arr(self, value):
        self._cumulative_arr = value
    @property
    def denomination(self):
        return self._denomination

    @denomination.setter
    def denomination(self, value):
        self._denomination = value
    @property
    def leads_code(self):
        return self._leads_code

    @leads_code.setter
    def leads_code(self, value):
        self._leads_code = value
    @property
    def ob_passport_id(self):
        return self._ob_passport_id

    @ob_passport_id.setter
    def ob_passport_id(self, value):
        self._ob_passport_id = value
    @property
    def pain_spot_list(self):
        return self._pain_spot_list

    @pain_spot_list.setter
    def pain_spot_list(self, value):
        if isinstance(value, list):
            self._pain_spot_list = list()
            for i in value:
                self._pain_spot_list.append(i)
    @property
    def reduction_reason(self):
        return self._reduction_reason

    @reduction_reason.setter
    def reduction_reason(self, value):
        self._reduction_reason = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def sales_force_id(self):
        return self._sales_force_id

    @sales_force_id.setter
    def sales_force_id(self, value):
        self._sales_force_id = value
    @property
    def third_party_passport_id(self):
        return self._third_party_passport_id

    @third_party_passport_id.setter
    def third_party_passport_id(self, value):
        self._third_party_passport_id = value
    @property
    def time_value(self):
        return self._time_value

    @time_value.setter
    def time_value(self, value):
        self._time_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_reason:
            if hasattr(self.apply_reason, 'to_alipay_dict'):
                params['apply_reason'] = self.apply_reason.to_alipay_dict()
            else:
                params['apply_reason'] = self.apply_reason
        if self.bd_work_no:
            if hasattr(self.bd_work_no, 'to_alipay_dict'):
                params['bd_work_no'] = self.bd_work_no.to_alipay_dict()
            else:
                params['bd_work_no'] = self.bd_work_no
        if self.comment:
            if hasattr(self.comment, 'to_alipay_dict'):
                params['comment'] = self.comment.to_alipay_dict()
            else:
                params['comment'] = self.comment
        if self.competitor_list:
            if isinstance(self.competitor_list, list):
                for i in range(0, len(self.competitor_list)):
                    element = self.competitor_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.competitor_list[i] = element.to_alipay_dict()
            if hasattr(self.competitor_list, 'to_alipay_dict'):
                params['competitor_list'] = self.competitor_list.to_alipay_dict()
            else:
                params['competitor_list'] = self.competitor_list
        if self.coupon_end_time:
            if hasattr(self.coupon_end_time, 'to_alipay_dict'):
                params['coupon_end_time'] = self.coupon_end_time.to_alipay_dict()
            else:
                params['coupon_end_time'] = self.coupon_end_time
        if self.coupon_name:
            if hasattr(self.coupon_name, 'to_alipay_dict'):
                params['coupon_name'] = self.coupon_name.to_alipay_dict()
            else:
                params['coupon_name'] = self.coupon_name
        if self.coupon_start_time:
            if hasattr(self.coupon_start_time, 'to_alipay_dict'):
                params['coupon_start_time'] = self.coupon_start_time.to_alipay_dict()
            else:
                params['coupon_start_time'] = self.coupon_start_time
        if self.coupon_validity_type:
            if hasattr(self.coupon_validity_type, 'to_alipay_dict'):
                params['coupon_validity_type'] = self.coupon_validity_type.to_alipay_dict()
            else:
                params['coupon_validity_type'] = self.coupon_validity_type
        if self.cumulative_arr:
            if hasattr(self.cumulative_arr, 'to_alipay_dict'):
                params['cumulative_arr'] = self.cumulative_arr.to_alipay_dict()
            else:
                params['cumulative_arr'] = self.cumulative_arr
        if self.denomination:
            if hasattr(self.denomination, 'to_alipay_dict'):
                params['denomination'] = self.denomination.to_alipay_dict()
            else:
                params['denomination'] = self.denomination
        if self.leads_code:
            if hasattr(self.leads_code, 'to_alipay_dict'):
                params['leads_code'] = self.leads_code.to_alipay_dict()
            else:
                params['leads_code'] = self.leads_code
        if self.ob_passport_id:
            if hasattr(self.ob_passport_id, 'to_alipay_dict'):
                params['ob_passport_id'] = self.ob_passport_id.to_alipay_dict()
            else:
                params['ob_passport_id'] = self.ob_passport_id
        if self.pain_spot_list:
            if isinstance(self.pain_spot_list, list):
                for i in range(0, len(self.pain_spot_list)):
                    element = self.pain_spot_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pain_spot_list[i] = element.to_alipay_dict()
            if hasattr(self.pain_spot_list, 'to_alipay_dict'):
                params['pain_spot_list'] = self.pain_spot_list.to_alipay_dict()
            else:
                params['pain_spot_list'] = self.pain_spot_list
        if self.reduction_reason:
            if hasattr(self.reduction_reason, 'to_alipay_dict'):
                params['reduction_reason'] = self.reduction_reason.to_alipay_dict()
            else:
                params['reduction_reason'] = self.reduction_reason
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        if self.sales_force_id:
            if hasattr(self.sales_force_id, 'to_alipay_dict'):
                params['sales_force_id'] = self.sales_force_id.to_alipay_dict()
            else:
                params['sales_force_id'] = self.sales_force_id
        if self.third_party_passport_id:
            if hasattr(self.third_party_passport_id, 'to_alipay_dict'):
                params['third_party_passport_id'] = self.third_party_passport_id.to_alipay_dict()
            else:
                params['third_party_passport_id'] = self.third_party_passport_id
        if self.time_value:
            if hasattr(self.time_value, 'to_alipay_dict'):
                params['time_value'] = self.time_value.to_alipay_dict()
            else:
                params['time_value'] = self.time_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalSfcloudfeereductionCreateModel()
        if 'apply_reason' in d:
            o.apply_reason = d['apply_reason']
        if 'bd_work_no' in d:
            o.bd_work_no = d['bd_work_no']
        if 'comment' in d:
            o.comment = d['comment']
        if 'competitor_list' in d:
            o.competitor_list = d['competitor_list']
        if 'coupon_end_time' in d:
            o.coupon_end_time = d['coupon_end_time']
        if 'coupon_name' in d:
            o.coupon_name = d['coupon_name']
        if 'coupon_start_time' in d:
            o.coupon_start_time = d['coupon_start_time']
        if 'coupon_validity_type' in d:
            o.coupon_validity_type = d['coupon_validity_type']
        if 'cumulative_arr' in d:
            o.cumulative_arr = d['cumulative_arr']
        if 'denomination' in d:
            o.denomination = d['denomination']
        if 'leads_code' in d:
            o.leads_code = d['leads_code']
        if 'ob_passport_id' in d:
            o.ob_passport_id = d['ob_passport_id']
        if 'pain_spot_list' in d:
            o.pain_spot_list = d['pain_spot_list']
        if 'reduction_reason' in d:
            o.reduction_reason = d['reduction_reason']
        if 'region' in d:
            o.region = d['region']
        if 'sales_force_id' in d:
            o.sales_force_id = d['sales_force_id']
        if 'third_party_passport_id' in d:
            o.third_party_passport_id = d['third_party_passport_id']
        if 'time_value' in d:
            o.time_value = d['time_value']
        return o


