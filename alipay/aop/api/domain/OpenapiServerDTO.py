#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecreateStatus import RecreateStatus


class OpenapiServerDTO(object):

    def __init__(self):
        self._cell = None
        self._hostname = None
        self._ip = None
        self._pod_name = None
        self._pod_no = None
        self._pod_uuid = None
        self._pod_version = None
        self._recreate_info = None
        self._release_status = None
        self._status = None
        self._update_time = None
        self._upgrade_progress = None

    @property
    def cell(self):
        return self._cell

    @cell.setter
    def cell(self, value):
        self._cell = value
    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self, value):
        self._hostname = value
    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value
    @property
    def pod_name(self):
        return self._pod_name

    @pod_name.setter
    def pod_name(self, value):
        self._pod_name = value
    @property
    def pod_no(self):
        return self._pod_no

    @pod_no.setter
    def pod_no(self, value):
        self._pod_no = value
    @property
    def pod_uuid(self):
        return self._pod_uuid

    @pod_uuid.setter
    def pod_uuid(self, value):
        self._pod_uuid = value
    @property
    def pod_version(self):
        return self._pod_version

    @pod_version.setter
    def pod_version(self, value):
        self._pod_version = value
    @property
    def recreate_info(self):
        return self._recreate_info

    @recreate_info.setter
    def recreate_info(self, value):
        if isinstance(value, RecreateStatus):
            self._recreate_info = value
        else:
            self._recreate_info = RecreateStatus.from_alipay_dict(value)
    @property
    def release_status(self):
        return self._release_status

    @release_status.setter
    def release_status(self, value):
        self._release_status = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value
    @property
    def upgrade_progress(self):
        return self._upgrade_progress

    @upgrade_progress.setter
    def upgrade_progress(self, value):
        self._upgrade_progress = value


    def to_alipay_dict(self):
        params = dict()
        if self.cell:
            if hasattr(self.cell, 'to_alipay_dict'):
                params['cell'] = self.cell.to_alipay_dict()
            else:
                params['cell'] = self.cell
        if self.hostname:
            if hasattr(self.hostname, 'to_alipay_dict'):
                params['hostname'] = self.hostname.to_alipay_dict()
            else:
                params['hostname'] = self.hostname
        if self.ip:
            if hasattr(self.ip, 'to_alipay_dict'):
                params['ip'] = self.ip.to_alipay_dict()
            else:
                params['ip'] = self.ip
        if self.pod_name:
            if hasattr(self.pod_name, 'to_alipay_dict'):
                params['pod_name'] = self.pod_name.to_alipay_dict()
            else:
                params['pod_name'] = self.pod_name
        if self.pod_no:
            if hasattr(self.pod_no, 'to_alipay_dict'):
                params['pod_no'] = self.pod_no.to_alipay_dict()
            else:
                params['pod_no'] = self.pod_no
        if self.pod_uuid:
            if hasattr(self.pod_uuid, 'to_alipay_dict'):
                params['pod_uuid'] = self.pod_uuid.to_alipay_dict()
            else:
                params['pod_uuid'] = self.pod_uuid
        if self.pod_version:
            if hasattr(self.pod_version, 'to_alipay_dict'):
                params['pod_version'] = self.pod_version.to_alipay_dict()
            else:
                params['pod_version'] = self.pod_version
        if self.recreate_info:
            if hasattr(self.recreate_info, 'to_alipay_dict'):
                params['recreate_info'] = self.recreate_info.to_alipay_dict()
            else:
                params['recreate_info'] = self.recreate_info
        if self.release_status:
            if hasattr(self.release_status, 'to_alipay_dict'):
                params['release_status'] = self.release_status.to_alipay_dict()
            else:
                params['release_status'] = self.release_status
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        if self.upgrade_progress:
            if hasattr(self.upgrade_progress, 'to_alipay_dict'):
                params['upgrade_progress'] = self.upgrade_progress.to_alipay_dict()
            else:
                params['upgrade_progress'] = self.upgrade_progress
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenapiServerDTO()
        if 'cell' in d:
            o.cell = d['cell']
        if 'hostname' in d:
            o.hostname = d['hostname']
        if 'ip' in d:
            o.ip = d['ip']
        if 'pod_name' in d:
            o.pod_name = d['pod_name']
        if 'pod_no' in d:
            o.pod_no = d['pod_no']
        if 'pod_uuid' in d:
            o.pod_uuid = d['pod_uuid']
        if 'pod_version' in d:
            o.pod_version = d['pod_version']
        if 'recreate_info' in d:
            o.recreate_info = d['recreate_info']
        if 'release_status' in d:
            o.release_status = d['release_status']
        if 'status' in d:
            o.status = d['status']
        if 'update_time' in d:
            o.update_time = d['update_time']
        if 'upgrade_progress' in d:
            o.upgrade_progress = d['upgrade_progress']
        return o


