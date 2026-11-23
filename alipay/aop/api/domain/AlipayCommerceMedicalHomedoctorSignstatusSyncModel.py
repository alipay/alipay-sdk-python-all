#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HomedoctorModifyProgressInfoDTO import HomedoctorModifyProgressInfoDTO
from alipay.aop.api.domain.HomedoctorRenewProgressInfoDTO import HomedoctorRenewProgressInfoDTO
from alipay.aop.api.domain.HomedoctorSignProgressInfoDTO import HomedoctorSignProgressInfoDTO
from alipay.aop.api.domain.HomedoctorTerminateProgressInfoDTO import HomedoctorTerminateProgressInfoDTO


class AlipayCommerceMedicalHomedoctorSignstatusSyncModel(object):

    def __init__(self):
        self._action = None
        self._card_name = None
        self._card_no = None
        self._cert_type = None
        self._modify_progress_info = None
        self._notify_time = None
        self._opt_serial_no = None
        self._renew_progress_info = None
        self._sign_biz_id = None
        self._sign_progress_info = None
        self._status = None
        self._terminate_progress_info = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def modify_progress_info(self):
        return self._modify_progress_info

    @modify_progress_info.setter
    def modify_progress_info(self, value):
        if isinstance(value, HomedoctorModifyProgressInfoDTO):
            self._modify_progress_info = value
        else:
            self._modify_progress_info = HomedoctorModifyProgressInfoDTO.from_alipay_dict(value)
    @property
    def notify_time(self):
        return self._notify_time

    @notify_time.setter
    def notify_time(self, value):
        self._notify_time = value
    @property
    def opt_serial_no(self):
        return self._opt_serial_no

    @opt_serial_no.setter
    def opt_serial_no(self, value):
        self._opt_serial_no = value
    @property
    def renew_progress_info(self):
        return self._renew_progress_info

    @renew_progress_info.setter
    def renew_progress_info(self, value):
        if isinstance(value, HomedoctorRenewProgressInfoDTO):
            self._renew_progress_info = value
        else:
            self._renew_progress_info = HomedoctorRenewProgressInfoDTO.from_alipay_dict(value)
    @property
    def sign_biz_id(self):
        return self._sign_biz_id

    @sign_biz_id.setter
    def sign_biz_id(self, value):
        self._sign_biz_id = value
    @property
    def sign_progress_info(self):
        return self._sign_progress_info

    @sign_progress_info.setter
    def sign_progress_info(self, value):
        if isinstance(value, HomedoctorSignProgressInfoDTO):
            self._sign_progress_info = value
        else:
            self._sign_progress_info = HomedoctorSignProgressInfoDTO.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def terminate_progress_info(self):
        return self._terminate_progress_info

    @terminate_progress_info.setter
    def terminate_progress_info(self, value):
        if isinstance(value, HomedoctorTerminateProgressInfoDTO):
            self._terminate_progress_info = value
        else:
            self._terminate_progress_info = HomedoctorTerminateProgressInfoDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = self.card_name.to_alipay_dict()
            else:
                params['card_name'] = self.card_name
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.modify_progress_info:
            if hasattr(self.modify_progress_info, 'to_alipay_dict'):
                params['modify_progress_info'] = self.modify_progress_info.to_alipay_dict()
            else:
                params['modify_progress_info'] = self.modify_progress_info
        if self.notify_time:
            if hasattr(self.notify_time, 'to_alipay_dict'):
                params['notify_time'] = self.notify_time.to_alipay_dict()
            else:
                params['notify_time'] = self.notify_time
        if self.opt_serial_no:
            if hasattr(self.opt_serial_no, 'to_alipay_dict'):
                params['opt_serial_no'] = self.opt_serial_no.to_alipay_dict()
            else:
                params['opt_serial_no'] = self.opt_serial_no
        if self.renew_progress_info:
            if hasattr(self.renew_progress_info, 'to_alipay_dict'):
                params['renew_progress_info'] = self.renew_progress_info.to_alipay_dict()
            else:
                params['renew_progress_info'] = self.renew_progress_info
        if self.sign_biz_id:
            if hasattr(self.sign_biz_id, 'to_alipay_dict'):
                params['sign_biz_id'] = self.sign_biz_id.to_alipay_dict()
            else:
                params['sign_biz_id'] = self.sign_biz_id
        if self.sign_progress_info:
            if hasattr(self.sign_progress_info, 'to_alipay_dict'):
                params['sign_progress_info'] = self.sign_progress_info.to_alipay_dict()
            else:
                params['sign_progress_info'] = self.sign_progress_info
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.terminate_progress_info:
            if hasattr(self.terminate_progress_info, 'to_alipay_dict'):
                params['terminate_progress_info'] = self.terminate_progress_info.to_alipay_dict()
            else:
                params['terminate_progress_info'] = self.terminate_progress_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHomedoctorSignstatusSyncModel()
        if 'action' in d:
            o.action = d['action']
        if 'card_name' in d:
            o.card_name = d['card_name']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'modify_progress_info' in d:
            o.modify_progress_info = d['modify_progress_info']
        if 'notify_time' in d:
            o.notify_time = d['notify_time']
        if 'opt_serial_no' in d:
            o.opt_serial_no = d['opt_serial_no']
        if 'renew_progress_info' in d:
            o.renew_progress_info = d['renew_progress_info']
        if 'sign_biz_id' in d:
            o.sign_biz_id = d['sign_biz_id']
        if 'sign_progress_info' in d:
            o.sign_progress_info = d['sign_progress_info']
        if 'status' in d:
            o.status = d['status']
        if 'terminate_progress_info' in d:
            o.terminate_progress_info = d['terminate_progress_info']
        return o


