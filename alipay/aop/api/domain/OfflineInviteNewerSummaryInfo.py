#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OfflineInviteNewerSummaryInfo(object):

    def __init__(self):
        self._ext_info = None
        self._partner_id = None
        self._pid = None
        self._report_date = None
        self._user_bind_card_count = None
        self._user_bind_card_settle_count = None
        self._user_cert_count = None
        self._user_cert_settle_count = None
        self._user_consume_count = None
        self._user_consume_settle_count = None
        self._user_prize_count = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
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
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def user_bind_card_count(self):
        return self._user_bind_card_count

    @user_bind_card_count.setter
    def user_bind_card_count(self, value):
        self._user_bind_card_count = value
    @property
    def user_bind_card_settle_count(self):
        return self._user_bind_card_settle_count

    @user_bind_card_settle_count.setter
    def user_bind_card_settle_count(self, value):
        self._user_bind_card_settle_count = value
    @property
    def user_cert_count(self):
        return self._user_cert_count

    @user_cert_count.setter
    def user_cert_count(self, value):
        self._user_cert_count = value
    @property
    def user_cert_settle_count(self):
        return self._user_cert_settle_count

    @user_cert_settle_count.setter
    def user_cert_settle_count(self, value):
        self._user_cert_settle_count = value
    @property
    def user_consume_count(self):
        return self._user_consume_count

    @user_consume_count.setter
    def user_consume_count(self, value):
        self._user_consume_count = value
    @property
    def user_consume_settle_count(self):
        return self._user_consume_settle_count

    @user_consume_settle_count.setter
    def user_consume_settle_count(self, value):
        self._user_consume_settle_count = value
    @property
    def user_prize_count(self):
        return self._user_prize_count

    @user_prize_count.setter
    def user_prize_count(self, value):
        self._user_prize_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
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
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        if self.user_bind_card_count:
            if hasattr(self.user_bind_card_count, 'to_alipay_dict'):
                params['user_bind_card_count'] = self.user_bind_card_count.to_alipay_dict()
            else:
                params['user_bind_card_count'] = self.user_bind_card_count
        if self.user_bind_card_settle_count:
            if hasattr(self.user_bind_card_settle_count, 'to_alipay_dict'):
                params['user_bind_card_settle_count'] = self.user_bind_card_settle_count.to_alipay_dict()
            else:
                params['user_bind_card_settle_count'] = self.user_bind_card_settle_count
        if self.user_cert_count:
            if hasattr(self.user_cert_count, 'to_alipay_dict'):
                params['user_cert_count'] = self.user_cert_count.to_alipay_dict()
            else:
                params['user_cert_count'] = self.user_cert_count
        if self.user_cert_settle_count:
            if hasattr(self.user_cert_settle_count, 'to_alipay_dict'):
                params['user_cert_settle_count'] = self.user_cert_settle_count.to_alipay_dict()
            else:
                params['user_cert_settle_count'] = self.user_cert_settle_count
        if self.user_consume_count:
            if hasattr(self.user_consume_count, 'to_alipay_dict'):
                params['user_consume_count'] = self.user_consume_count.to_alipay_dict()
            else:
                params['user_consume_count'] = self.user_consume_count
        if self.user_consume_settle_count:
            if hasattr(self.user_consume_settle_count, 'to_alipay_dict'):
                params['user_consume_settle_count'] = self.user_consume_settle_count.to_alipay_dict()
            else:
                params['user_consume_settle_count'] = self.user_consume_settle_count
        if self.user_prize_count:
            if hasattr(self.user_prize_count, 'to_alipay_dict'):
                params['user_prize_count'] = self.user_prize_count.to_alipay_dict()
            else:
                params['user_prize_count'] = self.user_prize_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OfflineInviteNewerSummaryInfo()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pid' in d:
            o.pid = d['pid']
        if 'report_date' in d:
            o.report_date = d['report_date']
        if 'user_bind_card_count' in d:
            o.user_bind_card_count = d['user_bind_card_count']
        if 'user_bind_card_settle_count' in d:
            o.user_bind_card_settle_count = d['user_bind_card_settle_count']
        if 'user_cert_count' in d:
            o.user_cert_count = d['user_cert_count']
        if 'user_cert_settle_count' in d:
            o.user_cert_settle_count = d['user_cert_settle_count']
        if 'user_consume_count' in d:
            o.user_consume_count = d['user_consume_count']
        if 'user_consume_settle_count' in d:
            o.user_consume_settle_count = d['user_consume_settle_count']
        if 'user_prize_count' in d:
            o.user_prize_count = d['user_prize_count']
        return o


