#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CrowdExportData(object):

    def __init__(self):
        self._biz_date = None
        self._biz_msg = None
        self._crowd_code = None
        self._export_channel_type = None
        self._oss_bucket = None
        self._oss_path = None
        self._uniq_biz_id = None
        self._user_count = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def biz_msg(self):
        return self._biz_msg

    @biz_msg.setter
    def biz_msg(self, value):
        self._biz_msg = value
    @property
    def crowd_code(self):
        return self._crowd_code

    @crowd_code.setter
    def crowd_code(self, value):
        self._crowd_code = value
    @property
    def export_channel_type(self):
        return self._export_channel_type

    @export_channel_type.setter
    def export_channel_type(self, value):
        self._export_channel_type = value
    @property
    def oss_bucket(self):
        return self._oss_bucket

    @oss_bucket.setter
    def oss_bucket(self, value):
        self._oss_bucket = value
    @property
    def oss_path(self):
        return self._oss_path

    @oss_path.setter
    def oss_path(self, value):
        self._oss_path = value
    @property
    def uniq_biz_id(self):
        return self._uniq_biz_id

    @uniq_biz_id.setter
    def uniq_biz_id(self, value):
        self._uniq_biz_id = value
    @property
    def user_count(self):
        return self._user_count

    @user_count.setter
    def user_count(self, value):
        self._user_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.biz_msg:
            if hasattr(self.biz_msg, 'to_alipay_dict'):
                params['biz_msg'] = self.biz_msg.to_alipay_dict()
            else:
                params['biz_msg'] = self.biz_msg
        if self.crowd_code:
            if hasattr(self.crowd_code, 'to_alipay_dict'):
                params['crowd_code'] = self.crowd_code.to_alipay_dict()
            else:
                params['crowd_code'] = self.crowd_code
        if self.export_channel_type:
            if hasattr(self.export_channel_type, 'to_alipay_dict'):
                params['export_channel_type'] = self.export_channel_type.to_alipay_dict()
            else:
                params['export_channel_type'] = self.export_channel_type
        if self.oss_bucket:
            if hasattr(self.oss_bucket, 'to_alipay_dict'):
                params['oss_bucket'] = self.oss_bucket.to_alipay_dict()
            else:
                params['oss_bucket'] = self.oss_bucket
        if self.oss_path:
            if hasattr(self.oss_path, 'to_alipay_dict'):
                params['oss_path'] = self.oss_path.to_alipay_dict()
            else:
                params['oss_path'] = self.oss_path
        if self.uniq_biz_id:
            if hasattr(self.uniq_biz_id, 'to_alipay_dict'):
                params['uniq_biz_id'] = self.uniq_biz_id.to_alipay_dict()
            else:
                params['uniq_biz_id'] = self.uniq_biz_id
        if self.user_count:
            if hasattr(self.user_count, 'to_alipay_dict'):
                params['user_count'] = self.user_count.to_alipay_dict()
            else:
                params['user_count'] = self.user_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CrowdExportData()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'biz_msg' in d:
            o.biz_msg = d['biz_msg']
        if 'crowd_code' in d:
            o.crowd_code = d['crowd_code']
        if 'export_channel_type' in d:
            o.export_channel_type = d['export_channel_type']
        if 'oss_bucket' in d:
            o.oss_bucket = d['oss_bucket']
        if 'oss_path' in d:
            o.oss_path = d['oss_path']
        if 'uniq_biz_id' in d:
            o.uniq_biz_id = d['uniq_biz_id']
        if 'user_count' in d:
            o.user_count = d['user_count']
        return o


