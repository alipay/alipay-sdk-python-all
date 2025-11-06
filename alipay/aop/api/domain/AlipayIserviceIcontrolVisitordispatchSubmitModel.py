#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIcontrolVisitordispatchSubmitModel(object):

    def __init__(self):
        self._biz_package_code = None
        self._channel = None
        self._channel_id = None
        self._ext_info = None
        self._origin_seat_id = None
        self._origin_service_uniq_code = None
        self._phone_number = None
        self._priority = None
        self._seat_id = None
        self._seat_type = None
        self._service_uniq_code = None
        self._skill_group_id = None
        self._skill_group_type = None
        self._source_sys = None
        self._tnt_inst_id = None
        self._visitor_id = None
        self._visitor_mode = None
        self._visitor_type = None

    @property
    def biz_package_code(self):
        return self._biz_package_code

    @biz_package_code.setter
    def biz_package_code(self, value):
        self._biz_package_code = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def origin_seat_id(self):
        return self._origin_seat_id

    @origin_seat_id.setter
    def origin_seat_id(self, value):
        self._origin_seat_id = value
    @property
    def origin_service_uniq_code(self):
        return self._origin_service_uniq_code

    @origin_service_uniq_code.setter
    def origin_service_uniq_code(self, value):
        self._origin_service_uniq_code = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value
    @property
    def seat_id(self):
        return self._seat_id

    @seat_id.setter
    def seat_id(self, value):
        self._seat_id = value
    @property
    def seat_type(self):
        return self._seat_type

    @seat_type.setter
    def seat_type(self, value):
        self._seat_type = value
    @property
    def service_uniq_code(self):
        return self._service_uniq_code

    @service_uniq_code.setter
    def service_uniq_code(self, value):
        self._service_uniq_code = value
    @property
    def skill_group_id(self):
        return self._skill_group_id

    @skill_group_id.setter
    def skill_group_id(self, value):
        self._skill_group_id = value
    @property
    def skill_group_type(self):
        return self._skill_group_type

    @skill_group_type.setter
    def skill_group_type(self, value):
        self._skill_group_type = value
    @property
    def source_sys(self):
        return self._source_sys

    @source_sys.setter
    def source_sys(self, value):
        self._source_sys = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def visitor_id(self):
        return self._visitor_id

    @visitor_id.setter
    def visitor_id(self, value):
        self._visitor_id = value
    @property
    def visitor_mode(self):
        return self._visitor_mode

    @visitor_mode.setter
    def visitor_mode(self, value):
        self._visitor_mode = value
    @property
    def visitor_type(self):
        return self._visitor_type

    @visitor_type.setter
    def visitor_type(self, value):
        self._visitor_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_package_code:
            if hasattr(self.biz_package_code, 'to_alipay_dict'):
                params['biz_package_code'] = self.biz_package_code.to_alipay_dict()
            else:
                params['biz_package_code'] = self.biz_package_code
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.origin_seat_id:
            if hasattr(self.origin_seat_id, 'to_alipay_dict'):
                params['origin_seat_id'] = self.origin_seat_id.to_alipay_dict()
            else:
                params['origin_seat_id'] = self.origin_seat_id
        if self.origin_service_uniq_code:
            if hasattr(self.origin_service_uniq_code, 'to_alipay_dict'):
                params['origin_service_uniq_code'] = self.origin_service_uniq_code.to_alipay_dict()
            else:
                params['origin_service_uniq_code'] = self.origin_service_uniq_code
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.priority:
            if hasattr(self.priority, 'to_alipay_dict'):
                params['priority'] = self.priority.to_alipay_dict()
            else:
                params['priority'] = self.priority
        if self.seat_id:
            if hasattr(self.seat_id, 'to_alipay_dict'):
                params['seat_id'] = self.seat_id.to_alipay_dict()
            else:
                params['seat_id'] = self.seat_id
        if self.seat_type:
            if hasattr(self.seat_type, 'to_alipay_dict'):
                params['seat_type'] = self.seat_type.to_alipay_dict()
            else:
                params['seat_type'] = self.seat_type
        if self.service_uniq_code:
            if hasattr(self.service_uniq_code, 'to_alipay_dict'):
                params['service_uniq_code'] = self.service_uniq_code.to_alipay_dict()
            else:
                params['service_uniq_code'] = self.service_uniq_code
        if self.skill_group_id:
            if hasattr(self.skill_group_id, 'to_alipay_dict'):
                params['skill_group_id'] = self.skill_group_id.to_alipay_dict()
            else:
                params['skill_group_id'] = self.skill_group_id
        if self.skill_group_type:
            if hasattr(self.skill_group_type, 'to_alipay_dict'):
                params['skill_group_type'] = self.skill_group_type.to_alipay_dict()
            else:
                params['skill_group_type'] = self.skill_group_type
        if self.source_sys:
            if hasattr(self.source_sys, 'to_alipay_dict'):
                params['source_sys'] = self.source_sys.to_alipay_dict()
            else:
                params['source_sys'] = self.source_sys
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.visitor_id:
            if hasattr(self.visitor_id, 'to_alipay_dict'):
                params['visitor_id'] = self.visitor_id.to_alipay_dict()
            else:
                params['visitor_id'] = self.visitor_id
        if self.visitor_mode:
            if hasattr(self.visitor_mode, 'to_alipay_dict'):
                params['visitor_mode'] = self.visitor_mode.to_alipay_dict()
            else:
                params['visitor_mode'] = self.visitor_mode
        if self.visitor_type:
            if hasattr(self.visitor_type, 'to_alipay_dict'):
                params['visitor_type'] = self.visitor_type.to_alipay_dict()
            else:
                params['visitor_type'] = self.visitor_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIcontrolVisitordispatchSubmitModel()
        if 'biz_package_code' in d:
            o.biz_package_code = d['biz_package_code']
        if 'channel' in d:
            o.channel = d['channel']
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'origin_seat_id' in d:
            o.origin_seat_id = d['origin_seat_id']
        if 'origin_service_uniq_code' in d:
            o.origin_service_uniq_code = d['origin_service_uniq_code']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'priority' in d:
            o.priority = d['priority']
        if 'seat_id' in d:
            o.seat_id = d['seat_id']
        if 'seat_type' in d:
            o.seat_type = d['seat_type']
        if 'service_uniq_code' in d:
            o.service_uniq_code = d['service_uniq_code']
        if 'skill_group_id' in d:
            o.skill_group_id = d['skill_group_id']
        if 'skill_group_type' in d:
            o.skill_group_type = d['skill_group_type']
        if 'source_sys' in d:
            o.source_sys = d['source_sys']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'visitor_id' in d:
            o.visitor_id = d['visitor_id']
        if 'visitor_mode' in d:
            o.visitor_mode = d['visitor_mode']
        if 'visitor_type' in d:
            o.visitor_type = d['visitor_type']
        return o


