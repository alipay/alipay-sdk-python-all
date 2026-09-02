#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsuranceReportinfoSyncModel(object):

    def __init__(self):
        self._assess_time = None
        self._biz_no = None
        self._channel = None
        self._ext_info = None
        self._fail_reason = None
        self._interpretation_person = None
        self._open_id = None
        self._out_unique_biz_no = None
        self._report_detail = None
        self._report_id = None
        self._report_image = None
        self._report_name = None
        self._status = None
        self._user_id = None

    @property
    def assess_time(self):
        return self._assess_time

    @assess_time.setter
    def assess_time(self, value):
        self._assess_time = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def interpretation_person(self):
        return self._interpretation_person

    @interpretation_person.setter
    def interpretation_person(self, value):
        self._interpretation_person = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_unique_biz_no(self):
        return self._out_unique_biz_no

    @out_unique_biz_no.setter
    def out_unique_biz_no(self, value):
        self._out_unique_biz_no = value
    @property
    def report_detail(self):
        return self._report_detail

    @report_detail.setter
    def report_detail(self, value):
        self._report_detail = value
    @property
    def report_id(self):
        return self._report_id

    @report_id.setter
    def report_id(self, value):
        self._report_id = value
    @property
    def report_image(self):
        return self._report_image

    @report_image.setter
    def report_image(self, value):
        self._report_image = value
    @property
    def report_name(self):
        return self._report_name

    @report_name.setter
    def report_name(self, value):
        self._report_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.assess_time:
            if hasattr(self.assess_time, 'to_alipay_dict'):
                params['assess_time'] = self.assess_time.to_alipay_dict()
            else:
                params['assess_time'] = self.assess_time
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.interpretation_person:
            if hasattr(self.interpretation_person, 'to_alipay_dict'):
                params['interpretation_person'] = self.interpretation_person.to_alipay_dict()
            else:
                params['interpretation_person'] = self.interpretation_person
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_unique_biz_no:
            if hasattr(self.out_unique_biz_no, 'to_alipay_dict'):
                params['out_unique_biz_no'] = self.out_unique_biz_no.to_alipay_dict()
            else:
                params['out_unique_biz_no'] = self.out_unique_biz_no
        if self.report_detail:
            if hasattr(self.report_detail, 'to_alipay_dict'):
                params['report_detail'] = self.report_detail.to_alipay_dict()
            else:
                params['report_detail'] = self.report_detail
        if self.report_id:
            if hasattr(self.report_id, 'to_alipay_dict'):
                params['report_id'] = self.report_id.to_alipay_dict()
            else:
                params['report_id'] = self.report_id
        if self.report_image:
            if hasattr(self.report_image, 'to_alipay_dict'):
                params['report_image'] = self.report_image.to_alipay_dict()
            else:
                params['report_image'] = self.report_image
        if self.report_name:
            if hasattr(self.report_name, 'to_alipay_dict'):
                params['report_name'] = self.report_name.to_alipay_dict()
            else:
                params['report_name'] = self.report_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceReportinfoSyncModel()
        if 'assess_time' in d:
            o.assess_time = d['assess_time']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'channel' in d:
            o.channel = d['channel']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'interpretation_person' in d:
            o.interpretation_person = d['interpretation_person']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_unique_biz_no' in d:
            o.out_unique_biz_no = d['out_unique_biz_no']
        if 'report_detail' in d:
            o.report_detail = d['report_detail']
        if 'report_id' in d:
            o.report_id = d['report_id']
        if 'report_image' in d:
            o.report_image = d['report_image']
        if 'report_name' in d:
            o.report_name = d['report_name']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


