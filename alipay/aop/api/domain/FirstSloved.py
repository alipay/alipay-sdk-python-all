#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FirstSloved(object):

    def __init__(self):
        self._agent_alipay_uid = None
        self._agent_nickname = None
        self._avg_response_length = None
        self._backflow_time = None
        self._business_name = None
        self._business_name_level_2 = None
        self._call_in_user_type = None
        self._cat_name_level_1 = None
        self._cat_name_level_2 = None
        self._cat_name_level_3 = None
        self._first_response_length = None
        self._gmt_create = None
        self._is_discontinue = None
        self._is_first_solved = None
        self._is_online_user_speak = None
        self._is_send = None
        self._report_date = None
        self._service_channel = None
        self._session_upgrade_time = None
        self._session_upgrade_type = None
        self._transfer_business_name = None
        self._transfer_cat_nam_level_2 = None
        self._transfer_cat_nam_level_3 = None
        self._transfer_servive_channel = None
        self._transfer_session_id = None
        self._transfer_user_order_id = None
        self._unresolved_reason = None
        self._upgrade_ticket_id = None
        self._user_guid = None
        self._user_order_id = None
        self._user_phone = None

    @property
    def agent_alipay_uid(self):
        return self._agent_alipay_uid

    @agent_alipay_uid.setter
    def agent_alipay_uid(self, value):
        self._agent_alipay_uid = value
    @property
    def agent_nickname(self):
        return self._agent_nickname

    @agent_nickname.setter
    def agent_nickname(self, value):
        self._agent_nickname = value
    @property
    def avg_response_length(self):
        return self._avg_response_length

    @avg_response_length.setter
    def avg_response_length(self, value):
        self._avg_response_length = value
    @property
    def backflow_time(self):
        return self._backflow_time

    @backflow_time.setter
    def backflow_time(self, value):
        self._backflow_time = value
    @property
    def business_name(self):
        return self._business_name

    @business_name.setter
    def business_name(self, value):
        self._business_name = value
    @property
    def business_name_level_2(self):
        return self._business_name_level_2

    @business_name_level_2.setter
    def business_name_level_2(self, value):
        self._business_name_level_2 = value
    @property
    def call_in_user_type(self):
        return self._call_in_user_type

    @call_in_user_type.setter
    def call_in_user_type(self, value):
        self._call_in_user_type = value
    @property
    def cat_name_level_1(self):
        return self._cat_name_level_1

    @cat_name_level_1.setter
    def cat_name_level_1(self, value):
        self._cat_name_level_1 = value
    @property
    def cat_name_level_2(self):
        return self._cat_name_level_2

    @cat_name_level_2.setter
    def cat_name_level_2(self, value):
        self._cat_name_level_2 = value
    @property
    def cat_name_level_3(self):
        return self._cat_name_level_3

    @cat_name_level_3.setter
    def cat_name_level_3(self, value):
        self._cat_name_level_3 = value
    @property
    def first_response_length(self):
        return self._first_response_length

    @first_response_length.setter
    def first_response_length(self, value):
        self._first_response_length = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def is_discontinue(self):
        return self._is_discontinue

    @is_discontinue.setter
    def is_discontinue(self, value):
        self._is_discontinue = value
    @property
    def is_first_solved(self):
        return self._is_first_solved

    @is_first_solved.setter
    def is_first_solved(self, value):
        self._is_first_solved = value
    @property
    def is_online_user_speak(self):
        return self._is_online_user_speak

    @is_online_user_speak.setter
    def is_online_user_speak(self, value):
        self._is_online_user_speak = value
    @property
    def is_send(self):
        return self._is_send

    @is_send.setter
    def is_send(self, value):
        self._is_send = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def service_channel(self):
        return self._service_channel

    @service_channel.setter
    def service_channel(self, value):
        self._service_channel = value
    @property
    def session_upgrade_time(self):
        return self._session_upgrade_time

    @session_upgrade_time.setter
    def session_upgrade_time(self, value):
        self._session_upgrade_time = value
    @property
    def session_upgrade_type(self):
        return self._session_upgrade_type

    @session_upgrade_type.setter
    def session_upgrade_type(self, value):
        self._session_upgrade_type = value
    @property
    def transfer_business_name(self):
        return self._transfer_business_name

    @transfer_business_name.setter
    def transfer_business_name(self, value):
        self._transfer_business_name = value
    @property
    def transfer_cat_nam_level_2(self):
        return self._transfer_cat_nam_level_2

    @transfer_cat_nam_level_2.setter
    def transfer_cat_nam_level_2(self, value):
        self._transfer_cat_nam_level_2 = value
    @property
    def transfer_cat_nam_level_3(self):
        return self._transfer_cat_nam_level_3

    @transfer_cat_nam_level_3.setter
    def transfer_cat_nam_level_3(self, value):
        self._transfer_cat_nam_level_3 = value
    @property
    def transfer_servive_channel(self):
        return self._transfer_servive_channel

    @transfer_servive_channel.setter
    def transfer_servive_channel(self, value):
        self._transfer_servive_channel = value
    @property
    def transfer_session_id(self):
        return self._transfer_session_id

    @transfer_session_id.setter
    def transfer_session_id(self, value):
        self._transfer_session_id = value
    @property
    def transfer_user_order_id(self):
        return self._transfer_user_order_id

    @transfer_user_order_id.setter
    def transfer_user_order_id(self, value):
        self._transfer_user_order_id = value
    @property
    def unresolved_reason(self):
        return self._unresolved_reason

    @unresolved_reason.setter
    def unresolved_reason(self, value):
        self._unresolved_reason = value
    @property
    def upgrade_ticket_id(self):
        return self._upgrade_ticket_id

    @upgrade_ticket_id.setter
    def upgrade_ticket_id(self, value):
        self._upgrade_ticket_id = value
    @property
    def user_guid(self):
        return self._user_guid

    @user_guid.setter
    def user_guid(self, value):
        self._user_guid = value
    @property
    def user_order_id(self):
        return self._user_order_id

    @user_order_id.setter
    def user_order_id(self, value):
        self._user_order_id = value
    @property
    def user_phone(self):
        return self._user_phone

    @user_phone.setter
    def user_phone(self, value):
        self._user_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_alipay_uid:
            if hasattr(self.agent_alipay_uid, 'to_alipay_dict'):
                params['agent_alipay_uid'] = self.agent_alipay_uid.to_alipay_dict()
            else:
                params['agent_alipay_uid'] = self.agent_alipay_uid
        if self.agent_nickname:
            if hasattr(self.agent_nickname, 'to_alipay_dict'):
                params['agent_nickname'] = self.agent_nickname.to_alipay_dict()
            else:
                params['agent_nickname'] = self.agent_nickname
        if self.avg_response_length:
            if hasattr(self.avg_response_length, 'to_alipay_dict'):
                params['avg_response_length'] = self.avg_response_length.to_alipay_dict()
            else:
                params['avg_response_length'] = self.avg_response_length
        if self.backflow_time:
            if hasattr(self.backflow_time, 'to_alipay_dict'):
                params['backflow_time'] = self.backflow_time.to_alipay_dict()
            else:
                params['backflow_time'] = self.backflow_time
        if self.business_name:
            if hasattr(self.business_name, 'to_alipay_dict'):
                params['business_name'] = self.business_name.to_alipay_dict()
            else:
                params['business_name'] = self.business_name
        if self.business_name_level_2:
            if hasattr(self.business_name_level_2, 'to_alipay_dict'):
                params['business_name_level_2'] = self.business_name_level_2.to_alipay_dict()
            else:
                params['business_name_level_2'] = self.business_name_level_2
        if self.call_in_user_type:
            if hasattr(self.call_in_user_type, 'to_alipay_dict'):
                params['call_in_user_type'] = self.call_in_user_type.to_alipay_dict()
            else:
                params['call_in_user_type'] = self.call_in_user_type
        if self.cat_name_level_1:
            if hasattr(self.cat_name_level_1, 'to_alipay_dict'):
                params['cat_name_level_1'] = self.cat_name_level_1.to_alipay_dict()
            else:
                params['cat_name_level_1'] = self.cat_name_level_1
        if self.cat_name_level_2:
            if hasattr(self.cat_name_level_2, 'to_alipay_dict'):
                params['cat_name_level_2'] = self.cat_name_level_2.to_alipay_dict()
            else:
                params['cat_name_level_2'] = self.cat_name_level_2
        if self.cat_name_level_3:
            if hasattr(self.cat_name_level_3, 'to_alipay_dict'):
                params['cat_name_level_3'] = self.cat_name_level_3.to_alipay_dict()
            else:
                params['cat_name_level_3'] = self.cat_name_level_3
        if self.first_response_length:
            if hasattr(self.first_response_length, 'to_alipay_dict'):
                params['first_response_length'] = self.first_response_length.to_alipay_dict()
            else:
                params['first_response_length'] = self.first_response_length
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.is_discontinue:
            if hasattr(self.is_discontinue, 'to_alipay_dict'):
                params['is_discontinue'] = self.is_discontinue.to_alipay_dict()
            else:
                params['is_discontinue'] = self.is_discontinue
        if self.is_first_solved:
            if hasattr(self.is_first_solved, 'to_alipay_dict'):
                params['is_first_solved'] = self.is_first_solved.to_alipay_dict()
            else:
                params['is_first_solved'] = self.is_first_solved
        if self.is_online_user_speak:
            if hasattr(self.is_online_user_speak, 'to_alipay_dict'):
                params['is_online_user_speak'] = self.is_online_user_speak.to_alipay_dict()
            else:
                params['is_online_user_speak'] = self.is_online_user_speak
        if self.is_send:
            if hasattr(self.is_send, 'to_alipay_dict'):
                params['is_send'] = self.is_send.to_alipay_dict()
            else:
                params['is_send'] = self.is_send
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        if self.service_channel:
            if hasattr(self.service_channel, 'to_alipay_dict'):
                params['service_channel'] = self.service_channel.to_alipay_dict()
            else:
                params['service_channel'] = self.service_channel
        if self.session_upgrade_time:
            if hasattr(self.session_upgrade_time, 'to_alipay_dict'):
                params['session_upgrade_time'] = self.session_upgrade_time.to_alipay_dict()
            else:
                params['session_upgrade_time'] = self.session_upgrade_time
        if self.session_upgrade_type:
            if hasattr(self.session_upgrade_type, 'to_alipay_dict'):
                params['session_upgrade_type'] = self.session_upgrade_type.to_alipay_dict()
            else:
                params['session_upgrade_type'] = self.session_upgrade_type
        if self.transfer_business_name:
            if hasattr(self.transfer_business_name, 'to_alipay_dict'):
                params['transfer_business_name'] = self.transfer_business_name.to_alipay_dict()
            else:
                params['transfer_business_name'] = self.transfer_business_name
        if self.transfer_cat_nam_level_2:
            if hasattr(self.transfer_cat_nam_level_2, 'to_alipay_dict'):
                params['transfer_cat_nam_level_2'] = self.transfer_cat_nam_level_2.to_alipay_dict()
            else:
                params['transfer_cat_nam_level_2'] = self.transfer_cat_nam_level_2
        if self.transfer_cat_nam_level_3:
            if hasattr(self.transfer_cat_nam_level_3, 'to_alipay_dict'):
                params['transfer_cat_nam_level_3'] = self.transfer_cat_nam_level_3.to_alipay_dict()
            else:
                params['transfer_cat_nam_level_3'] = self.transfer_cat_nam_level_3
        if self.transfer_servive_channel:
            if hasattr(self.transfer_servive_channel, 'to_alipay_dict'):
                params['transfer_servive_channel'] = self.transfer_servive_channel.to_alipay_dict()
            else:
                params['transfer_servive_channel'] = self.transfer_servive_channel
        if self.transfer_session_id:
            if hasattr(self.transfer_session_id, 'to_alipay_dict'):
                params['transfer_session_id'] = self.transfer_session_id.to_alipay_dict()
            else:
                params['transfer_session_id'] = self.transfer_session_id
        if self.transfer_user_order_id:
            if hasattr(self.transfer_user_order_id, 'to_alipay_dict'):
                params['transfer_user_order_id'] = self.transfer_user_order_id.to_alipay_dict()
            else:
                params['transfer_user_order_id'] = self.transfer_user_order_id
        if self.unresolved_reason:
            if hasattr(self.unresolved_reason, 'to_alipay_dict'):
                params['unresolved_reason'] = self.unresolved_reason.to_alipay_dict()
            else:
                params['unresolved_reason'] = self.unresolved_reason
        if self.upgrade_ticket_id:
            if hasattr(self.upgrade_ticket_id, 'to_alipay_dict'):
                params['upgrade_ticket_id'] = self.upgrade_ticket_id.to_alipay_dict()
            else:
                params['upgrade_ticket_id'] = self.upgrade_ticket_id
        if self.user_guid:
            if hasattr(self.user_guid, 'to_alipay_dict'):
                params['user_guid'] = self.user_guid.to_alipay_dict()
            else:
                params['user_guid'] = self.user_guid
        if self.user_order_id:
            if hasattr(self.user_order_id, 'to_alipay_dict'):
                params['user_order_id'] = self.user_order_id.to_alipay_dict()
            else:
                params['user_order_id'] = self.user_order_id
        if self.user_phone:
            if hasattr(self.user_phone, 'to_alipay_dict'):
                params['user_phone'] = self.user_phone.to_alipay_dict()
            else:
                params['user_phone'] = self.user_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FirstSloved()
        if 'agent_alipay_uid' in d:
            o.agent_alipay_uid = d['agent_alipay_uid']
        if 'agent_nickname' in d:
            o.agent_nickname = d['agent_nickname']
        if 'avg_response_length' in d:
            o.avg_response_length = d['avg_response_length']
        if 'backflow_time' in d:
            o.backflow_time = d['backflow_time']
        if 'business_name' in d:
            o.business_name = d['business_name']
        if 'business_name_level_2' in d:
            o.business_name_level_2 = d['business_name_level_2']
        if 'call_in_user_type' in d:
            o.call_in_user_type = d['call_in_user_type']
        if 'cat_name_level_1' in d:
            o.cat_name_level_1 = d['cat_name_level_1']
        if 'cat_name_level_2' in d:
            o.cat_name_level_2 = d['cat_name_level_2']
        if 'cat_name_level_3' in d:
            o.cat_name_level_3 = d['cat_name_level_3']
        if 'first_response_length' in d:
            o.first_response_length = d['first_response_length']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'is_discontinue' in d:
            o.is_discontinue = d['is_discontinue']
        if 'is_first_solved' in d:
            o.is_first_solved = d['is_first_solved']
        if 'is_online_user_speak' in d:
            o.is_online_user_speak = d['is_online_user_speak']
        if 'is_send' in d:
            o.is_send = d['is_send']
        if 'report_date' in d:
            o.report_date = d['report_date']
        if 'service_channel' in d:
            o.service_channel = d['service_channel']
        if 'session_upgrade_time' in d:
            o.session_upgrade_time = d['session_upgrade_time']
        if 'session_upgrade_type' in d:
            o.session_upgrade_type = d['session_upgrade_type']
        if 'transfer_business_name' in d:
            o.transfer_business_name = d['transfer_business_name']
        if 'transfer_cat_nam_level_2' in d:
            o.transfer_cat_nam_level_2 = d['transfer_cat_nam_level_2']
        if 'transfer_cat_nam_level_3' in d:
            o.transfer_cat_nam_level_3 = d['transfer_cat_nam_level_3']
        if 'transfer_servive_channel' in d:
            o.transfer_servive_channel = d['transfer_servive_channel']
        if 'transfer_session_id' in d:
            o.transfer_session_id = d['transfer_session_id']
        if 'transfer_user_order_id' in d:
            o.transfer_user_order_id = d['transfer_user_order_id']
        if 'unresolved_reason' in d:
            o.unresolved_reason = d['unresolved_reason']
        if 'upgrade_ticket_id' in d:
            o.upgrade_ticket_id = d['upgrade_ticket_id']
        if 'user_guid' in d:
            o.user_guid = d['user_guid']
        if 'user_order_id' in d:
            o.user_order_id = d['user_order_id']
        if 'user_phone' in d:
            o.user_phone = d['user_phone']
        return o


