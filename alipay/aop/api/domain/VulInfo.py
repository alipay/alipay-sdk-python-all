#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VulInfo(object):

    def __init__(self):
        self._attachment = None
        self._business = None
        self._coin = None
        self._company = None
        self._confirm_level = None
        self._confirm_time = None
        self._detail = None
        self._fix_time = None
        self._level = None
        self._mobile_phone = None
        self._name = None
        self._nick = None
        self._reject_reason = None
        self._score = None
        self._status = None
        self._submit_time = None
        self._type_sub_first_id = None
        self._type_sub_first_name = None
        self._type_sub_second_id = None
        self._type_sub_second_name = None
        self._url = None
        self._vul_id = None

    @property
    def attachment(self):
        return self._attachment

    @attachment.setter
    def attachment(self, value):
        self._attachment = value
    @property
    def business(self):
        return self._business

    @business.setter
    def business(self, value):
        self._business = value
    @property
    def coin(self):
        return self._coin

    @coin.setter
    def coin(self, value):
        self._coin = value
    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value
    @property
    def confirm_level(self):
        return self._confirm_level

    @confirm_level.setter
    def confirm_level(self, value):
        self._confirm_level = value
    @property
    def confirm_time(self):
        return self._confirm_time

    @confirm_time.setter
    def confirm_time(self, value):
        self._confirm_time = value
    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        self._detail = value
    @property
    def fix_time(self):
        return self._fix_time

    @fix_time.setter
    def fix_time(self, value):
        self._fix_time = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def mobile_phone(self):
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        self._mobile_phone = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def nick(self):
        return self._nick

    @nick.setter
    def nick(self, value):
        self._nick = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def submit_time(self):
        return self._submit_time

    @submit_time.setter
    def submit_time(self, value):
        self._submit_time = value
    @property
    def type_sub_first_id(self):
        return self._type_sub_first_id

    @type_sub_first_id.setter
    def type_sub_first_id(self, value):
        self._type_sub_first_id = value
    @property
    def type_sub_first_name(self):
        return self._type_sub_first_name

    @type_sub_first_name.setter
    def type_sub_first_name(self, value):
        self._type_sub_first_name = value
    @property
    def type_sub_second_id(self):
        return self._type_sub_second_id

    @type_sub_second_id.setter
    def type_sub_second_id(self, value):
        self._type_sub_second_id = value
    @property
    def type_sub_second_name(self):
        return self._type_sub_second_name

    @type_sub_second_name.setter
    def type_sub_second_name(self, value):
        self._type_sub_second_name = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
    @property
    def vul_id(self):
        return self._vul_id

    @vul_id.setter
    def vul_id(self, value):
        self._vul_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment:
            if hasattr(self.attachment, 'to_alipay_dict'):
                params['attachment'] = self.attachment.to_alipay_dict()
            else:
                params['attachment'] = self.attachment
        if self.business:
            if hasattr(self.business, 'to_alipay_dict'):
                params['business'] = self.business.to_alipay_dict()
            else:
                params['business'] = self.business
        if self.coin:
            if hasattr(self.coin, 'to_alipay_dict'):
                params['coin'] = self.coin.to_alipay_dict()
            else:
                params['coin'] = self.coin
        if self.company:
            if hasattr(self.company, 'to_alipay_dict'):
                params['company'] = self.company.to_alipay_dict()
            else:
                params['company'] = self.company
        if self.confirm_level:
            if hasattr(self.confirm_level, 'to_alipay_dict'):
                params['confirm_level'] = self.confirm_level.to_alipay_dict()
            else:
                params['confirm_level'] = self.confirm_level
        if self.confirm_time:
            if hasattr(self.confirm_time, 'to_alipay_dict'):
                params['confirm_time'] = self.confirm_time.to_alipay_dict()
            else:
                params['confirm_time'] = self.confirm_time
        if self.detail:
            if hasattr(self.detail, 'to_alipay_dict'):
                params['detail'] = self.detail.to_alipay_dict()
            else:
                params['detail'] = self.detail
        if self.fix_time:
            if hasattr(self.fix_time, 'to_alipay_dict'):
                params['fix_time'] = self.fix_time.to_alipay_dict()
            else:
                params['fix_time'] = self.fix_time
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.mobile_phone:
            if hasattr(self.mobile_phone, 'to_alipay_dict'):
                params['mobile_phone'] = self.mobile_phone.to_alipay_dict()
            else:
                params['mobile_phone'] = self.mobile_phone
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.nick:
            if hasattr(self.nick, 'to_alipay_dict'):
                params['nick'] = self.nick.to_alipay_dict()
            else:
                params['nick'] = self.nick
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.submit_time:
            if hasattr(self.submit_time, 'to_alipay_dict'):
                params['submit_time'] = self.submit_time.to_alipay_dict()
            else:
                params['submit_time'] = self.submit_time
        if self.type_sub_first_id:
            if hasattr(self.type_sub_first_id, 'to_alipay_dict'):
                params['type_sub_first_id'] = self.type_sub_first_id.to_alipay_dict()
            else:
                params['type_sub_first_id'] = self.type_sub_first_id
        if self.type_sub_first_name:
            if hasattr(self.type_sub_first_name, 'to_alipay_dict'):
                params['type_sub_first_name'] = self.type_sub_first_name.to_alipay_dict()
            else:
                params['type_sub_first_name'] = self.type_sub_first_name
        if self.type_sub_second_id:
            if hasattr(self.type_sub_second_id, 'to_alipay_dict'):
                params['type_sub_second_id'] = self.type_sub_second_id.to_alipay_dict()
            else:
                params['type_sub_second_id'] = self.type_sub_second_id
        if self.type_sub_second_name:
            if hasattr(self.type_sub_second_name, 'to_alipay_dict'):
                params['type_sub_second_name'] = self.type_sub_second_name.to_alipay_dict()
            else:
                params['type_sub_second_name'] = self.type_sub_second_name
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        if self.vul_id:
            if hasattr(self.vul_id, 'to_alipay_dict'):
                params['vul_id'] = self.vul_id.to_alipay_dict()
            else:
                params['vul_id'] = self.vul_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VulInfo()
        if 'attachment' in d:
            o.attachment = d['attachment']
        if 'business' in d:
            o.business = d['business']
        if 'coin' in d:
            o.coin = d['coin']
        if 'company' in d:
            o.company = d['company']
        if 'confirm_level' in d:
            o.confirm_level = d['confirm_level']
        if 'confirm_time' in d:
            o.confirm_time = d['confirm_time']
        if 'detail' in d:
            o.detail = d['detail']
        if 'fix_time' in d:
            o.fix_time = d['fix_time']
        if 'level' in d:
            o.level = d['level']
        if 'mobile_phone' in d:
            o.mobile_phone = d['mobile_phone']
        if 'name' in d:
            o.name = d['name']
        if 'nick' in d:
            o.nick = d['nick']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        if 'score' in d:
            o.score = d['score']
        if 'status' in d:
            o.status = d['status']
        if 'submit_time' in d:
            o.submit_time = d['submit_time']
        if 'type_sub_first_id' in d:
            o.type_sub_first_id = d['type_sub_first_id']
        if 'type_sub_first_name' in d:
            o.type_sub_first_name = d['type_sub_first_name']
        if 'type_sub_second_id' in d:
            o.type_sub_second_id = d['type_sub_second_id']
        if 'type_sub_second_name' in d:
            o.type_sub_second_name = d['type_sub_second_name']
        if 'url' in d:
            o.url = d['url']
        if 'vul_id' in d:
            o.vul_id = d['vul_id']
        return o


