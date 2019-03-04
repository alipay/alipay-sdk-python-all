#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingCampaignMemberRelationBindModel(object):

    def __init__(self):
        self._activate_time = None
        self._balance = None
        self._birth = None
        self._cell = None
        self._end_time = None
        self._gender = None
        self._level = None
        self._member_template_id = None
        self._out_member_no = None
        self._point = None
        self._request_id = None
        self._start_time = None
        self._user_id = None
        self._user_name = None

    @property
    def activate_time(self):
        return self._activate_time

    @activate_time.setter
    def activate_time(self, value):
        self._activate_time = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value
    @property
    def cell(self):
        return self._cell

    @cell.setter
    def cell(self, value):
        self._cell = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def member_template_id(self):
        return self._member_template_id

    @member_template_id.setter
    def member_template_id(self, value):
        self._member_template_id = value
    @property
    def out_member_no(self):
        return self._out_member_no

    @out_member_no.setter
    def out_member_no(self, value):
        self._out_member_no = value
    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.activate_time:
            if hasattr(self.activate_time, 'to_alipay_dict'):
                params['activate_time'] = self.activate_time.to_alipay_dict()
            else:
                params['activate_time'] = self.activate_time
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.birth:
            if hasattr(self.birth, 'to_alipay_dict'):
                params['birth'] = self.birth.to_alipay_dict()
            else:
                params['birth'] = self.birth
        if self.cell:
            if hasattr(self.cell, 'to_alipay_dict'):
                params['cell'] = self.cell.to_alipay_dict()
            else:
                params['cell'] = self.cell
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.member_template_id:
            if hasattr(self.member_template_id, 'to_alipay_dict'):
                params['member_template_id'] = self.member_template_id.to_alipay_dict()
            else:
                params['member_template_id'] = self.member_template_id
        if self.out_member_no:
            if hasattr(self.out_member_no, 'to_alipay_dict'):
                params['out_member_no'] = self.out_member_no.to_alipay_dict()
            else:
                params['out_member_no'] = self.out_member_no
        if self.point:
            if hasattr(self.point, 'to_alipay_dict'):
                params['point'] = self.point.to_alipay_dict()
            else:
                params['point'] = self.point
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignMemberRelationBindModel()
        if 'activate_time' in d:
            o.activate_time = d['activate_time']
        if 'balance' in d:
            o.balance = d['balance']
        if 'birth' in d:
            o.birth = d['birth']
        if 'cell' in d:
            o.cell = d['cell']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'gender' in d:
            o.gender = d['gender']
        if 'level' in d:
            o.level = d['level']
        if 'member_template_id' in d:
            o.member_template_id = d['member_template_id']
        if 'out_member_no' in d:
            o.out_member_no = d['out_member_no']
        if 'point' in d:
            o.point = d['point']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


