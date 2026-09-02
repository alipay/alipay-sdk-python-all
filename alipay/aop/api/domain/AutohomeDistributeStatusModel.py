#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AutohomeDistributeStatusModel(object):

    def __init__(self):
        self._clues_distribute_state = None
        self._clues_push_stime = None
        self._deal_series_id = None
        self._deal_status = None
        self._deal_time = None
        self._direct_distribute_fail_detail_reason = None
        self._direct_distribute_fail_reason = None
        self._direct_distribute_state = None
        self._direct_distribute_time = None
        self._dist_time = None
        self._distribute_fail_detail_reason = None
        self._distribute_fail_reason = None
        self._first_touch = None
        self._key_activity_id = None
        self._key_business_id = None
        self._key_car_age = None
        self._key_car_all_case = None
        self._key_car_audi_id = None
        self._key_car_img_url = None
        self._key_distributor_id = None
        self._key_ext_1 = None
        self._key_need_business_name = None
        self._key_phone_hashcode = None
        self._key_supply_business_id = None
        self._last_modified_stime = None
        self._split_count = None

    @property
    def clues_distribute_state(self):
        return self._clues_distribute_state

    @clues_distribute_state.setter
    def clues_distribute_state(self, value):
        self._clues_distribute_state = value
    @property
    def clues_push_stime(self):
        return self._clues_push_stime

    @clues_push_stime.setter
    def clues_push_stime(self, value):
        self._clues_push_stime = value
    @property
    def deal_series_id(self):
        return self._deal_series_id

    @deal_series_id.setter
    def deal_series_id(self, value):
        self._deal_series_id = value
    @property
    def deal_status(self):
        return self._deal_status

    @deal_status.setter
    def deal_status(self, value):
        self._deal_status = value
    @property
    def deal_time(self):
        return self._deal_time

    @deal_time.setter
    def deal_time(self, value):
        self._deal_time = value
    @property
    def direct_distribute_fail_detail_reason(self):
        return self._direct_distribute_fail_detail_reason

    @direct_distribute_fail_detail_reason.setter
    def direct_distribute_fail_detail_reason(self, value):
        self._direct_distribute_fail_detail_reason = value
    @property
    def direct_distribute_fail_reason(self):
        return self._direct_distribute_fail_reason

    @direct_distribute_fail_reason.setter
    def direct_distribute_fail_reason(self, value):
        self._direct_distribute_fail_reason = value
    @property
    def direct_distribute_state(self):
        return self._direct_distribute_state

    @direct_distribute_state.setter
    def direct_distribute_state(self, value):
        self._direct_distribute_state = value
    @property
    def direct_distribute_time(self):
        return self._direct_distribute_time

    @direct_distribute_time.setter
    def direct_distribute_time(self, value):
        self._direct_distribute_time = value
    @property
    def dist_time(self):
        return self._dist_time

    @dist_time.setter
    def dist_time(self, value):
        self._dist_time = value
    @property
    def distribute_fail_detail_reason(self):
        return self._distribute_fail_detail_reason

    @distribute_fail_detail_reason.setter
    def distribute_fail_detail_reason(self, value):
        self._distribute_fail_detail_reason = value
    @property
    def distribute_fail_reason(self):
        return self._distribute_fail_reason

    @distribute_fail_reason.setter
    def distribute_fail_reason(self, value):
        self._distribute_fail_reason = value
    @property
    def first_touch(self):
        return self._first_touch

    @first_touch.setter
    def first_touch(self, value):
        self._first_touch = value
    @property
    def key_activity_id(self):
        return self._key_activity_id

    @key_activity_id.setter
    def key_activity_id(self, value):
        self._key_activity_id = value
    @property
    def key_business_id(self):
        return self._key_business_id

    @key_business_id.setter
    def key_business_id(self, value):
        self._key_business_id = value
    @property
    def key_car_age(self):
        return self._key_car_age

    @key_car_age.setter
    def key_car_age(self, value):
        self._key_car_age = value
    @property
    def key_car_all_case(self):
        return self._key_car_all_case

    @key_car_all_case.setter
    def key_car_all_case(self, value):
        self._key_car_all_case = value
    @property
    def key_car_audi_id(self):
        return self._key_car_audi_id

    @key_car_audi_id.setter
    def key_car_audi_id(self, value):
        self._key_car_audi_id = value
    @property
    def key_car_img_url(self):
        return self._key_car_img_url

    @key_car_img_url.setter
    def key_car_img_url(self, value):
        self._key_car_img_url = value
    @property
    def key_distributor_id(self):
        return self._key_distributor_id

    @key_distributor_id.setter
    def key_distributor_id(self, value):
        self._key_distributor_id = value
    @property
    def key_ext_1(self):
        return self._key_ext_1

    @key_ext_1.setter
    def key_ext_1(self, value):
        self._key_ext_1 = value
    @property
    def key_need_business_name(self):
        return self._key_need_business_name

    @key_need_business_name.setter
    def key_need_business_name(self, value):
        self._key_need_business_name = value
    @property
    def key_phone_hashcode(self):
        return self._key_phone_hashcode

    @key_phone_hashcode.setter
    def key_phone_hashcode(self, value):
        self._key_phone_hashcode = value
    @property
    def key_supply_business_id(self):
        return self._key_supply_business_id

    @key_supply_business_id.setter
    def key_supply_business_id(self, value):
        self._key_supply_business_id = value
    @property
    def last_modified_stime(self):
        return self._last_modified_stime

    @last_modified_stime.setter
    def last_modified_stime(self, value):
        self._last_modified_stime = value
    @property
    def split_count(self):
        return self._split_count

    @split_count.setter
    def split_count(self, value):
        self._split_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.clues_distribute_state:
            if hasattr(self.clues_distribute_state, 'to_alipay_dict'):
                params['clues_distribute_state'] = self.clues_distribute_state.to_alipay_dict()
            else:
                params['clues_distribute_state'] = self.clues_distribute_state
        if self.clues_push_stime:
            if hasattr(self.clues_push_stime, 'to_alipay_dict'):
                params['clues_push_stime'] = self.clues_push_stime.to_alipay_dict()
            else:
                params['clues_push_stime'] = self.clues_push_stime
        if self.deal_series_id:
            if hasattr(self.deal_series_id, 'to_alipay_dict'):
                params['deal_series_id'] = self.deal_series_id.to_alipay_dict()
            else:
                params['deal_series_id'] = self.deal_series_id
        if self.deal_status:
            if hasattr(self.deal_status, 'to_alipay_dict'):
                params['deal_status'] = self.deal_status.to_alipay_dict()
            else:
                params['deal_status'] = self.deal_status
        if self.deal_time:
            if hasattr(self.deal_time, 'to_alipay_dict'):
                params['deal_time'] = self.deal_time.to_alipay_dict()
            else:
                params['deal_time'] = self.deal_time
        if self.direct_distribute_fail_detail_reason:
            if hasattr(self.direct_distribute_fail_detail_reason, 'to_alipay_dict'):
                params['direct_distribute_fail_detail_reason'] = self.direct_distribute_fail_detail_reason.to_alipay_dict()
            else:
                params['direct_distribute_fail_detail_reason'] = self.direct_distribute_fail_detail_reason
        if self.direct_distribute_fail_reason:
            if hasattr(self.direct_distribute_fail_reason, 'to_alipay_dict'):
                params['direct_distribute_fail_reason'] = self.direct_distribute_fail_reason.to_alipay_dict()
            else:
                params['direct_distribute_fail_reason'] = self.direct_distribute_fail_reason
        if self.direct_distribute_state:
            if hasattr(self.direct_distribute_state, 'to_alipay_dict'):
                params['direct_distribute_state'] = self.direct_distribute_state.to_alipay_dict()
            else:
                params['direct_distribute_state'] = self.direct_distribute_state
        if self.direct_distribute_time:
            if hasattr(self.direct_distribute_time, 'to_alipay_dict'):
                params['direct_distribute_time'] = self.direct_distribute_time.to_alipay_dict()
            else:
                params['direct_distribute_time'] = self.direct_distribute_time
        if self.dist_time:
            if hasattr(self.dist_time, 'to_alipay_dict'):
                params['dist_time'] = self.dist_time.to_alipay_dict()
            else:
                params['dist_time'] = self.dist_time
        if self.distribute_fail_detail_reason:
            if hasattr(self.distribute_fail_detail_reason, 'to_alipay_dict'):
                params['distribute_fail_detail_reason'] = self.distribute_fail_detail_reason.to_alipay_dict()
            else:
                params['distribute_fail_detail_reason'] = self.distribute_fail_detail_reason
        if self.distribute_fail_reason:
            if hasattr(self.distribute_fail_reason, 'to_alipay_dict'):
                params['distribute_fail_reason'] = self.distribute_fail_reason.to_alipay_dict()
            else:
                params['distribute_fail_reason'] = self.distribute_fail_reason
        if self.first_touch:
            if hasattr(self.first_touch, 'to_alipay_dict'):
                params['first_touch'] = self.first_touch.to_alipay_dict()
            else:
                params['first_touch'] = self.first_touch
        if self.key_activity_id:
            if hasattr(self.key_activity_id, 'to_alipay_dict'):
                params['key_activity_id'] = self.key_activity_id.to_alipay_dict()
            else:
                params['key_activity_id'] = self.key_activity_id
        if self.key_business_id:
            if hasattr(self.key_business_id, 'to_alipay_dict'):
                params['key_business_id'] = self.key_business_id.to_alipay_dict()
            else:
                params['key_business_id'] = self.key_business_id
        if self.key_car_age:
            if hasattr(self.key_car_age, 'to_alipay_dict'):
                params['key_car_age'] = self.key_car_age.to_alipay_dict()
            else:
                params['key_car_age'] = self.key_car_age
        if self.key_car_all_case:
            if hasattr(self.key_car_all_case, 'to_alipay_dict'):
                params['key_car_all_case'] = self.key_car_all_case.to_alipay_dict()
            else:
                params['key_car_all_case'] = self.key_car_all_case
        if self.key_car_audi_id:
            if hasattr(self.key_car_audi_id, 'to_alipay_dict'):
                params['key_car_audi_id'] = self.key_car_audi_id.to_alipay_dict()
            else:
                params['key_car_audi_id'] = self.key_car_audi_id
        if self.key_car_img_url:
            if hasattr(self.key_car_img_url, 'to_alipay_dict'):
                params['key_car_img_url'] = self.key_car_img_url.to_alipay_dict()
            else:
                params['key_car_img_url'] = self.key_car_img_url
        if self.key_distributor_id:
            if hasattr(self.key_distributor_id, 'to_alipay_dict'):
                params['key_distributor_id'] = self.key_distributor_id.to_alipay_dict()
            else:
                params['key_distributor_id'] = self.key_distributor_id
        if self.key_ext_1:
            if hasattr(self.key_ext_1, 'to_alipay_dict'):
                params['key_ext_1'] = self.key_ext_1.to_alipay_dict()
            else:
                params['key_ext_1'] = self.key_ext_1
        if self.key_need_business_name:
            if hasattr(self.key_need_business_name, 'to_alipay_dict'):
                params['key_need_business_name'] = self.key_need_business_name.to_alipay_dict()
            else:
                params['key_need_business_name'] = self.key_need_business_name
        if self.key_phone_hashcode:
            if hasattr(self.key_phone_hashcode, 'to_alipay_dict'):
                params['key_phone_hashcode'] = self.key_phone_hashcode.to_alipay_dict()
            else:
                params['key_phone_hashcode'] = self.key_phone_hashcode
        if self.key_supply_business_id:
            if hasattr(self.key_supply_business_id, 'to_alipay_dict'):
                params['key_supply_business_id'] = self.key_supply_business_id.to_alipay_dict()
            else:
                params['key_supply_business_id'] = self.key_supply_business_id
        if self.last_modified_stime:
            if hasattr(self.last_modified_stime, 'to_alipay_dict'):
                params['last_modified_stime'] = self.last_modified_stime.to_alipay_dict()
            else:
                params['last_modified_stime'] = self.last_modified_stime
        if self.split_count:
            if hasattr(self.split_count, 'to_alipay_dict'):
                params['split_count'] = self.split_count.to_alipay_dict()
            else:
                params['split_count'] = self.split_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AutohomeDistributeStatusModel()
        if 'clues_distribute_state' in d:
            o.clues_distribute_state = d['clues_distribute_state']
        if 'clues_push_stime' in d:
            o.clues_push_stime = d['clues_push_stime']
        if 'deal_series_id' in d:
            o.deal_series_id = d['deal_series_id']
        if 'deal_status' in d:
            o.deal_status = d['deal_status']
        if 'deal_time' in d:
            o.deal_time = d['deal_time']
        if 'direct_distribute_fail_detail_reason' in d:
            o.direct_distribute_fail_detail_reason = d['direct_distribute_fail_detail_reason']
        if 'direct_distribute_fail_reason' in d:
            o.direct_distribute_fail_reason = d['direct_distribute_fail_reason']
        if 'direct_distribute_state' in d:
            o.direct_distribute_state = d['direct_distribute_state']
        if 'direct_distribute_time' in d:
            o.direct_distribute_time = d['direct_distribute_time']
        if 'dist_time' in d:
            o.dist_time = d['dist_time']
        if 'distribute_fail_detail_reason' in d:
            o.distribute_fail_detail_reason = d['distribute_fail_detail_reason']
        if 'distribute_fail_reason' in d:
            o.distribute_fail_reason = d['distribute_fail_reason']
        if 'first_touch' in d:
            o.first_touch = d['first_touch']
        if 'key_activity_id' in d:
            o.key_activity_id = d['key_activity_id']
        if 'key_business_id' in d:
            o.key_business_id = d['key_business_id']
        if 'key_car_age' in d:
            o.key_car_age = d['key_car_age']
        if 'key_car_all_case' in d:
            o.key_car_all_case = d['key_car_all_case']
        if 'key_car_audi_id' in d:
            o.key_car_audi_id = d['key_car_audi_id']
        if 'key_car_img_url' in d:
            o.key_car_img_url = d['key_car_img_url']
        if 'key_distributor_id' in d:
            o.key_distributor_id = d['key_distributor_id']
        if 'key_ext_1' in d:
            o.key_ext_1 = d['key_ext_1']
        if 'key_need_business_name' in d:
            o.key_need_business_name = d['key_need_business_name']
        if 'key_phone_hashcode' in d:
            o.key_phone_hashcode = d['key_phone_hashcode']
        if 'key_supply_business_id' in d:
            o.key_supply_business_id = d['key_supply_business_id']
        if 'last_modified_stime' in d:
            o.last_modified_stime = d['last_modified_stime']
        if 'split_count' in d:
            o.split_count = d['split_count']
        return o


