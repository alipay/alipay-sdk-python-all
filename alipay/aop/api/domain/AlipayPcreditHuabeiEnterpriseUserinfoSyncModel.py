#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiEnterpriseUserinfoSyncModel(object):

    def __init__(self):
        self._agreement_id = None
        self._alipay_user_id = None
        self._dept_name = None
        self._employee_count = None
        self._employee_level = None
        self._employee_name = None
        self._employee_position = None
        self._entry_time = None
        self._identity_no = None
        self._mail_addr = None
        self._management = None
        self._mobile_no = None
        self._partner_id = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def dept_name(self):
        return self._dept_name

    @dept_name.setter
    def dept_name(self, value):
        self._dept_name = value
    @property
    def employee_count(self):
        return self._employee_count

    @employee_count.setter
    def employee_count(self, value):
        self._employee_count = value
    @property
    def employee_level(self):
        return self._employee_level

    @employee_level.setter
    def employee_level(self, value):
        self._employee_level = value
    @property
    def employee_name(self):
        return self._employee_name

    @employee_name.setter
    def employee_name(self, value):
        self._employee_name = value
    @property
    def employee_position(self):
        return self._employee_position

    @employee_position.setter
    def employee_position(self, value):
        self._employee_position = value
    @property
    def entry_time(self):
        return self._entry_time

    @entry_time.setter
    def entry_time(self, value):
        self._entry_time = value
    @property
    def identity_no(self):
        return self._identity_no

    @identity_no.setter
    def identity_no(self, value):
        self._identity_no = value
    @property
    def mail_addr(self):
        return self._mail_addr

    @mail_addr.setter
    def mail_addr(self, value):
        self._mail_addr = value
    @property
    def management(self):
        return self._management

    @management.setter
    def management(self, value):
        self._management = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_id:
            if hasattr(self.agreement_id, 'to_alipay_dict'):
                params['agreement_id'] = self.agreement_id.to_alipay_dict()
            else:
                params['agreement_id'] = self.agreement_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.dept_name:
            if hasattr(self.dept_name, 'to_alipay_dict'):
                params['dept_name'] = self.dept_name.to_alipay_dict()
            else:
                params['dept_name'] = self.dept_name
        if self.employee_count:
            if hasattr(self.employee_count, 'to_alipay_dict'):
                params['employee_count'] = self.employee_count.to_alipay_dict()
            else:
                params['employee_count'] = self.employee_count
        if self.employee_level:
            if hasattr(self.employee_level, 'to_alipay_dict'):
                params['employee_level'] = self.employee_level.to_alipay_dict()
            else:
                params['employee_level'] = self.employee_level
        if self.employee_name:
            if hasattr(self.employee_name, 'to_alipay_dict'):
                params['employee_name'] = self.employee_name.to_alipay_dict()
            else:
                params['employee_name'] = self.employee_name
        if self.employee_position:
            if hasattr(self.employee_position, 'to_alipay_dict'):
                params['employee_position'] = self.employee_position.to_alipay_dict()
            else:
                params['employee_position'] = self.employee_position
        if self.entry_time:
            if hasattr(self.entry_time, 'to_alipay_dict'):
                params['entry_time'] = self.entry_time.to_alipay_dict()
            else:
                params['entry_time'] = self.entry_time
        if self.identity_no:
            if hasattr(self.identity_no, 'to_alipay_dict'):
                params['identity_no'] = self.identity_no.to_alipay_dict()
            else:
                params['identity_no'] = self.identity_no
        if self.mail_addr:
            if hasattr(self.mail_addr, 'to_alipay_dict'):
                params['mail_addr'] = self.mail_addr.to_alipay_dict()
            else:
                params['mail_addr'] = self.mail_addr
        if self.management:
            if hasattr(self.management, 'to_alipay_dict'):
                params['management'] = self.management.to_alipay_dict()
            else:
                params['management'] = self.management
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiEnterpriseUserinfoSyncModel()
        if 'agreement_id' in d:
            o.agreement_id = d['agreement_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'dept_name' in d:
            o.dept_name = d['dept_name']
        if 'employee_count' in d:
            o.employee_count = d['employee_count']
        if 'employee_level' in d:
            o.employee_level = d['employee_level']
        if 'employee_name' in d:
            o.employee_name = d['employee_name']
        if 'employee_position' in d:
            o.employee_position = d['employee_position']
        if 'entry_time' in d:
            o.entry_time = d['entry_time']
        if 'identity_no' in d:
            o.identity_no = d['identity_no']
        if 'mail_addr' in d:
            o.mail_addr = d['mail_addr']
        if 'management' in d:
            o.management = d['management']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        return o


