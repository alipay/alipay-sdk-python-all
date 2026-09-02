#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HospitalConfigItem import HospitalConfigItem
from alipay.aop.api.domain.HospitalConfigItem import HospitalConfigItem
from alipay.aop.api.domain.HospitalConfigItem import HospitalConfigItem
from alipay.aop.api.domain.HospitalConfigItem import HospitalConfigItem
from alipay.aop.api.domain.HospitalConfigItem import HospitalConfigItem
from alipay.aop.api.domain.HospitalConfigItem import HospitalConfigItem
from alipay.aop.api.domain.BianqueJumpChainConfig import BianqueJumpChainConfig
from alipay.aop.api.domain.HospitalConfigItem import HospitalConfigItem
from alipay.aop.api.domain.HospitalConfigItem import HospitalConfigItem
from alipay.aop.api.domain.HospitalConfigItem import HospitalConfigItem
from alipay.aop.api.domain.HospitalConfigItem import HospitalConfigItem
from alipay.aop.api.domain.HospitalConfigItem import HospitalConfigItem


class BianqueConfigItem(object):

    def __init__(self):
        self._afu_no_subscribe_msg_enabled = None
        self._check_appointment_enabled = None
        self._cloud_consult_afu_enabled = None
        self._institutional_source = None
        self._online_register_enabled = None
        self._online_sign_in_enabled = None
        self._payment_access_enabled = None
        self._payment_access_mode = None
        self._payment_jump_config = None
        self._payment_jump_support_medical = None
        self._payment_medical_enabled = None
        self._register_access_enabled = None
        self._register_access_mode = None
        self._report_access_enabled = None
        self._report_access_mode = None
        self._unified_social_credit_code = None

    @property
    def afu_no_subscribe_msg_enabled(self):
        return self._afu_no_subscribe_msg_enabled

    @afu_no_subscribe_msg_enabled.setter
    def afu_no_subscribe_msg_enabled(self, value):
        if isinstance(value, HospitalConfigItem):
            self._afu_no_subscribe_msg_enabled = value
        else:
            self._afu_no_subscribe_msg_enabled = HospitalConfigItem.from_alipay_dict(value)
    @property
    def check_appointment_enabled(self):
        return self._check_appointment_enabled

    @check_appointment_enabled.setter
    def check_appointment_enabled(self, value):
        if isinstance(value, HospitalConfigItem):
            self._check_appointment_enabled = value
        else:
            self._check_appointment_enabled = HospitalConfigItem.from_alipay_dict(value)
    @property
    def cloud_consult_afu_enabled(self):
        return self._cloud_consult_afu_enabled

    @cloud_consult_afu_enabled.setter
    def cloud_consult_afu_enabled(self, value):
        if isinstance(value, HospitalConfigItem):
            self._cloud_consult_afu_enabled = value
        else:
            self._cloud_consult_afu_enabled = HospitalConfigItem.from_alipay_dict(value)
    @property
    def institutional_source(self):
        return self._institutional_source

    @institutional_source.setter
    def institutional_source(self, value):
        self._institutional_source = value
    @property
    def online_register_enabled(self):
        return self._online_register_enabled

    @online_register_enabled.setter
    def online_register_enabled(self, value):
        if isinstance(value, HospitalConfigItem):
            self._online_register_enabled = value
        else:
            self._online_register_enabled = HospitalConfigItem.from_alipay_dict(value)
    @property
    def online_sign_in_enabled(self):
        return self._online_sign_in_enabled

    @online_sign_in_enabled.setter
    def online_sign_in_enabled(self, value):
        if isinstance(value, list):
            self._online_sign_in_enabled = list()
            for i in value:
                if isinstance(i, HospitalConfigItem):
                    self._online_sign_in_enabled.append(i)
                else:
                    self._online_sign_in_enabled.append(HospitalConfigItem.from_alipay_dict(i))
    @property
    def payment_access_enabled(self):
        return self._payment_access_enabled

    @payment_access_enabled.setter
    def payment_access_enabled(self, value):
        if isinstance(value, HospitalConfigItem):
            self._payment_access_enabled = value
        else:
            self._payment_access_enabled = HospitalConfigItem.from_alipay_dict(value)
    @property
    def payment_access_mode(self):
        return self._payment_access_mode

    @payment_access_mode.setter
    def payment_access_mode(self, value):
        self._payment_access_mode = value
    @property
    def payment_jump_config(self):
        return self._payment_jump_config

    @payment_jump_config.setter
    def payment_jump_config(self, value):
        if isinstance(value, list):
            self._payment_jump_config = list()
            for i in value:
                if isinstance(i, BianqueJumpChainConfig):
                    self._payment_jump_config.append(i)
                else:
                    self._payment_jump_config.append(BianqueJumpChainConfig.from_alipay_dict(i))
    @property
    def payment_jump_support_medical(self):
        return self._payment_jump_support_medical

    @payment_jump_support_medical.setter
    def payment_jump_support_medical(self, value):
        if isinstance(value, HospitalConfigItem):
            self._payment_jump_support_medical = value
        else:
            self._payment_jump_support_medical = HospitalConfigItem.from_alipay_dict(value)
    @property
    def payment_medical_enabled(self):
        return self._payment_medical_enabled

    @payment_medical_enabled.setter
    def payment_medical_enabled(self, value):
        if isinstance(value, HospitalConfigItem):
            self._payment_medical_enabled = value
        else:
            self._payment_medical_enabled = HospitalConfigItem.from_alipay_dict(value)
    @property
    def register_access_enabled(self):
        return self._register_access_enabled

    @register_access_enabled.setter
    def register_access_enabled(self, value):
        if isinstance(value, HospitalConfigItem):
            self._register_access_enabled = value
        else:
            self._register_access_enabled = HospitalConfigItem.from_alipay_dict(value)
    @property
    def register_access_mode(self):
        return self._register_access_mode

    @register_access_mode.setter
    def register_access_mode(self, value):
        self._register_access_mode = value
    @property
    def report_access_enabled(self):
        return self._report_access_enabled

    @report_access_enabled.setter
    def report_access_enabled(self, value):
        if isinstance(value, list):
            self._report_access_enabled = list()
            for i in value:
                if isinstance(i, HospitalConfigItem):
                    self._report_access_enabled.append(i)
                else:
                    self._report_access_enabled.append(HospitalConfigItem.from_alipay_dict(i))
    @property
    def report_access_mode(self):
        return self._report_access_mode

    @report_access_mode.setter
    def report_access_mode(self, value):
        if isinstance(value, list):
            self._report_access_mode = list()
            for i in value:
                if isinstance(i, HospitalConfigItem):
                    self._report_access_mode.append(i)
                else:
                    self._report_access_mode.append(HospitalConfigItem.from_alipay_dict(i))
    @property
    def unified_social_credit_code(self):
        return self._unified_social_credit_code

    @unified_social_credit_code.setter
    def unified_social_credit_code(self, value):
        self._unified_social_credit_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.afu_no_subscribe_msg_enabled:
            if hasattr(self.afu_no_subscribe_msg_enabled, 'to_alipay_dict'):
                params['afu_no_subscribe_msg_enabled'] = self.afu_no_subscribe_msg_enabled.to_alipay_dict()
            else:
                params['afu_no_subscribe_msg_enabled'] = self.afu_no_subscribe_msg_enabled
        if self.check_appointment_enabled:
            if hasattr(self.check_appointment_enabled, 'to_alipay_dict'):
                params['check_appointment_enabled'] = self.check_appointment_enabled.to_alipay_dict()
            else:
                params['check_appointment_enabled'] = self.check_appointment_enabled
        if self.cloud_consult_afu_enabled:
            if hasattr(self.cloud_consult_afu_enabled, 'to_alipay_dict'):
                params['cloud_consult_afu_enabled'] = self.cloud_consult_afu_enabled.to_alipay_dict()
            else:
                params['cloud_consult_afu_enabled'] = self.cloud_consult_afu_enabled
        if self.institutional_source:
            if hasattr(self.institutional_source, 'to_alipay_dict'):
                params['institutional_source'] = self.institutional_source.to_alipay_dict()
            else:
                params['institutional_source'] = self.institutional_source
        if self.online_register_enabled:
            if hasattr(self.online_register_enabled, 'to_alipay_dict'):
                params['online_register_enabled'] = self.online_register_enabled.to_alipay_dict()
            else:
                params['online_register_enabled'] = self.online_register_enabled
        if self.online_sign_in_enabled:
            if isinstance(self.online_sign_in_enabled, list):
                for i in range(0, len(self.online_sign_in_enabled)):
                    element = self.online_sign_in_enabled[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.online_sign_in_enabled[i] = element.to_alipay_dict()
            if hasattr(self.online_sign_in_enabled, 'to_alipay_dict'):
                params['online_sign_in_enabled'] = self.online_sign_in_enabled.to_alipay_dict()
            else:
                params['online_sign_in_enabled'] = self.online_sign_in_enabled
        if self.payment_access_enabled:
            if hasattr(self.payment_access_enabled, 'to_alipay_dict'):
                params['payment_access_enabled'] = self.payment_access_enabled.to_alipay_dict()
            else:
                params['payment_access_enabled'] = self.payment_access_enabled
        if self.payment_access_mode:
            if hasattr(self.payment_access_mode, 'to_alipay_dict'):
                params['payment_access_mode'] = self.payment_access_mode.to_alipay_dict()
            else:
                params['payment_access_mode'] = self.payment_access_mode
        if self.payment_jump_config:
            if isinstance(self.payment_jump_config, list):
                for i in range(0, len(self.payment_jump_config)):
                    element = self.payment_jump_config[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.payment_jump_config[i] = element.to_alipay_dict()
            if hasattr(self.payment_jump_config, 'to_alipay_dict'):
                params['payment_jump_config'] = self.payment_jump_config.to_alipay_dict()
            else:
                params['payment_jump_config'] = self.payment_jump_config
        if self.payment_jump_support_medical:
            if hasattr(self.payment_jump_support_medical, 'to_alipay_dict'):
                params['payment_jump_support_medical'] = self.payment_jump_support_medical.to_alipay_dict()
            else:
                params['payment_jump_support_medical'] = self.payment_jump_support_medical
        if self.payment_medical_enabled:
            if hasattr(self.payment_medical_enabled, 'to_alipay_dict'):
                params['payment_medical_enabled'] = self.payment_medical_enabled.to_alipay_dict()
            else:
                params['payment_medical_enabled'] = self.payment_medical_enabled
        if self.register_access_enabled:
            if hasattr(self.register_access_enabled, 'to_alipay_dict'):
                params['register_access_enabled'] = self.register_access_enabled.to_alipay_dict()
            else:
                params['register_access_enabled'] = self.register_access_enabled
        if self.register_access_mode:
            if hasattr(self.register_access_mode, 'to_alipay_dict'):
                params['register_access_mode'] = self.register_access_mode.to_alipay_dict()
            else:
                params['register_access_mode'] = self.register_access_mode
        if self.report_access_enabled:
            if isinstance(self.report_access_enabled, list):
                for i in range(0, len(self.report_access_enabled)):
                    element = self.report_access_enabled[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.report_access_enabled[i] = element.to_alipay_dict()
            if hasattr(self.report_access_enabled, 'to_alipay_dict'):
                params['report_access_enabled'] = self.report_access_enabled.to_alipay_dict()
            else:
                params['report_access_enabled'] = self.report_access_enabled
        if self.report_access_mode:
            if isinstance(self.report_access_mode, list):
                for i in range(0, len(self.report_access_mode)):
                    element = self.report_access_mode[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.report_access_mode[i] = element.to_alipay_dict()
            if hasattr(self.report_access_mode, 'to_alipay_dict'):
                params['report_access_mode'] = self.report_access_mode.to_alipay_dict()
            else:
                params['report_access_mode'] = self.report_access_mode
        if self.unified_social_credit_code:
            if hasattr(self.unified_social_credit_code, 'to_alipay_dict'):
                params['unified_social_credit_code'] = self.unified_social_credit_code.to_alipay_dict()
            else:
                params['unified_social_credit_code'] = self.unified_social_credit_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BianqueConfigItem()
        if 'afu_no_subscribe_msg_enabled' in d:
            o.afu_no_subscribe_msg_enabled = d['afu_no_subscribe_msg_enabled']
        if 'check_appointment_enabled' in d:
            o.check_appointment_enabled = d['check_appointment_enabled']
        if 'cloud_consult_afu_enabled' in d:
            o.cloud_consult_afu_enabled = d['cloud_consult_afu_enabled']
        if 'institutional_source' in d:
            o.institutional_source = d['institutional_source']
        if 'online_register_enabled' in d:
            o.online_register_enabled = d['online_register_enabled']
        if 'online_sign_in_enabled' in d:
            o.online_sign_in_enabled = d['online_sign_in_enabled']
        if 'payment_access_enabled' in d:
            o.payment_access_enabled = d['payment_access_enabled']
        if 'payment_access_mode' in d:
            o.payment_access_mode = d['payment_access_mode']
        if 'payment_jump_config' in d:
            o.payment_jump_config = d['payment_jump_config']
        if 'payment_jump_support_medical' in d:
            o.payment_jump_support_medical = d['payment_jump_support_medical']
        if 'payment_medical_enabled' in d:
            o.payment_medical_enabled = d['payment_medical_enabled']
        if 'register_access_enabled' in d:
            o.register_access_enabled = d['register_access_enabled']
        if 'register_access_mode' in d:
            o.register_access_mode = d['register_access_mode']
        if 'report_access_enabled' in d:
            o.report_access_enabled = d['report_access_enabled']
        if 'report_access_mode' in d:
            o.report_access_mode = d['report_access_mode']
        if 'unified_social_credit_code' in d:
            o.unified_social_credit_code = d['unified_social_credit_code']
        return o


