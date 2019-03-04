#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OfflineInviteNewerDetailInfo(object):

    def __init__(self):
        self._invited_phone = None
        self._partner_id = None
        self._pid = None
        self._settled = None
        self._settled_and_bind = None
        self._user_bind_card_time = None
        self._user_cert_time = None
        self._user_prize_time = None

    @property
    def invited_phone(self):
        return self._invited_phone

    @invited_phone.setter
    def invited_phone(self, value):
        self._invited_phone = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def settled(self):
        return self._settled

    @settled.setter
    def settled(self, value):
        self._settled = value
    @property
    def settled_and_bind(self):
        return self._settled_and_bind

    @settled_and_bind.setter
    def settled_and_bind(self, value):
        self._settled_and_bind = value
    @property
    def user_bind_card_time(self):
        return self._user_bind_card_time

    @user_bind_card_time.setter
    def user_bind_card_time(self, value):
        self._user_bind_card_time = value
    @property
    def user_cert_time(self):
        return self._user_cert_time

    @user_cert_time.setter
    def user_cert_time(self, value):
        self._user_cert_time = value
    @property
    def user_prize_time(self):
        return self._user_prize_time

    @user_prize_time.setter
    def user_prize_time(self, value):
        self._user_prize_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.invited_phone:
            if hasattr(self.invited_phone, 'to_alipay_dict'):
                params['invited_phone'] = self.invited_phone.to_alipay_dict()
            else:
                params['invited_phone'] = self.invited_phone
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.settled:
            if hasattr(self.settled, 'to_alipay_dict'):
                params['settled'] = self.settled.to_alipay_dict()
            else:
                params['settled'] = self.settled
        if self.settled_and_bind:
            if hasattr(self.settled_and_bind, 'to_alipay_dict'):
                params['settled_and_bind'] = self.settled_and_bind.to_alipay_dict()
            else:
                params['settled_and_bind'] = self.settled_and_bind
        if self.user_bind_card_time:
            if hasattr(self.user_bind_card_time, 'to_alipay_dict'):
                params['user_bind_card_time'] = self.user_bind_card_time.to_alipay_dict()
            else:
                params['user_bind_card_time'] = self.user_bind_card_time
        if self.user_cert_time:
            if hasattr(self.user_cert_time, 'to_alipay_dict'):
                params['user_cert_time'] = self.user_cert_time.to_alipay_dict()
            else:
                params['user_cert_time'] = self.user_cert_time
        if self.user_prize_time:
            if hasattr(self.user_prize_time, 'to_alipay_dict'):
                params['user_prize_time'] = self.user_prize_time.to_alipay_dict()
            else:
                params['user_prize_time'] = self.user_prize_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OfflineInviteNewerDetailInfo()
        if 'invited_phone' in d:
            o.invited_phone = d['invited_phone']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'settled' in d:
            o.settled = d['settled']
        if 'settled_and_bind' in d:
            o.settled_and_bind = d['settled_and_bind']
        if 'user_bind_card_time' in d:
            o.user_bind_card_time = d['user_bind_card_time']
        if 'user_cert_time' in d:
            o.user_cert_time = d['user_cert_time']
        if 'user_prize_time' in d:
            o.user_prize_time = d['user_prize_time']
        return o


