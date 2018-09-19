#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ArrangementBaseVO(object):

    def __init__(self):
        self._app_id = None
        self._arrangement_institution_code = None
        self._arrangement_name = None
        self._arrangement_no = None
        self._arrangement_type = None
        self._arrangement_version = None
        self._channel_code = None
        self._gmt_end = None
        self._gmt_expired = None
        self._gmt_invalid_due = None
        self._gmt_sign = None
        self._gmt_vald_due = None
        self._gmt_vrsn = None
        self._ip_role_id = None
        self._last_moder = None
        self._mark_type = None
        self._memo = None
        self._moder_type = None
        self._pd_mark = None
        self._prod_code = None
        self._prod_name = None
        self._prod_version = None
        self._ps_code = None
        self._ps_id = None
        self._ps_name = None
        self._status = None
        self._template_prod_code = None
        self._template_prod_version = None

    @property
    def app_id(self):
        return self._app_id

    @app_id.setter
    def app_id(self, value):
        self._app_id = value
    @property
    def arrangement_institution_code(self):
        return self._arrangement_institution_code

    @arrangement_institution_code.setter
    def arrangement_institution_code(self, value):
        self._arrangement_institution_code = value
    @property
    def arrangement_name(self):
        return self._arrangement_name

    @arrangement_name.setter
    def arrangement_name(self, value):
        self._arrangement_name = value
    @property
    def arrangement_no(self):
        return self._arrangement_no

    @arrangement_no.setter
    def arrangement_no(self, value):
        self._arrangement_no = value
    @property
    def arrangement_type(self):
        return self._arrangement_type

    @arrangement_type.setter
    def arrangement_type(self, value):
        self._arrangement_type = value
    @property
    def arrangement_version(self):
        return self._arrangement_version

    @arrangement_version.setter
    def arrangement_version(self, value):
        self._arrangement_version = value
    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_expired(self):
        return self._gmt_expired

    @gmt_expired.setter
    def gmt_expired(self, value):
        self._gmt_expired = value
    @property
    def gmt_invalid_due(self):
        return self._gmt_invalid_due

    @gmt_invalid_due.setter
    def gmt_invalid_due(self, value):
        self._gmt_invalid_due = value
    @property
    def gmt_sign(self):
        return self._gmt_sign

    @gmt_sign.setter
    def gmt_sign(self, value):
        self._gmt_sign = value
    @property
    def gmt_vald_due(self):
        return self._gmt_vald_due

    @gmt_vald_due.setter
    def gmt_vald_due(self, value):
        self._gmt_vald_due = value
    @property
    def gmt_vrsn(self):
        return self._gmt_vrsn

    @gmt_vrsn.setter
    def gmt_vrsn(self, value):
        self._gmt_vrsn = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def last_moder(self):
        return self._last_moder

    @last_moder.setter
    def last_moder(self, value):
        self._last_moder = value
    @property
    def mark_type(self):
        return self._mark_type

    @mark_type.setter
    def mark_type(self, value):
        self._mark_type = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def moder_type(self):
        return self._moder_type

    @moder_type.setter
    def moder_type(self, value):
        self._moder_type = value
    @property
    def pd_mark(self):
        return self._pd_mark

    @pd_mark.setter
    def pd_mark(self, value):
        self._pd_mark = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def prod_name(self):
        return self._prod_name

    @prod_name.setter
    def prod_name(self, value):
        self._prod_name = value
    @property
    def prod_version(self):
        return self._prod_version

    @prod_version.setter
    def prod_version(self, value):
        self._prod_version = value
    @property
    def ps_code(self):
        return self._ps_code

    @ps_code.setter
    def ps_code(self, value):
        self._ps_code = value
    @property
    def ps_id(self):
        return self._ps_id

    @ps_id.setter
    def ps_id(self, value):
        self._ps_id = value
    @property
    def ps_name(self):
        return self._ps_name

    @ps_name.setter
    def ps_name(self, value):
        self._ps_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_prod_code(self):
        return self._template_prod_code

    @template_prod_code.setter
    def template_prod_code(self, value):
        self._template_prod_code = value
    @property
    def template_prod_version(self):
        return self._template_prod_version

    @template_prod_version.setter
    def template_prod_version(self, value):
        self._template_prod_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_id:
            if hasattr(self.app_id, 'to_alipay_dict'):
                params['app_id'] = self.app_id.to_alipay_dict()
            else:
                params['app_id'] = self.app_id
        if self.arrangement_institution_code:
            if hasattr(self.arrangement_institution_code, 'to_alipay_dict'):
                params['arrangement_institution_code'] = self.arrangement_institution_code.to_alipay_dict()
            else:
                params['arrangement_institution_code'] = self.arrangement_institution_code
        if self.arrangement_name:
            if hasattr(self.arrangement_name, 'to_alipay_dict'):
                params['arrangement_name'] = self.arrangement_name.to_alipay_dict()
            else:
                params['arrangement_name'] = self.arrangement_name
        if self.arrangement_no:
            if hasattr(self.arrangement_no, 'to_alipay_dict'):
                params['arrangement_no'] = self.arrangement_no.to_alipay_dict()
            else:
                params['arrangement_no'] = self.arrangement_no
        if self.arrangement_type:
            if hasattr(self.arrangement_type, 'to_alipay_dict'):
                params['arrangement_type'] = self.arrangement_type.to_alipay_dict()
            else:
                params['arrangement_type'] = self.arrangement_type
        if self.arrangement_version:
            if hasattr(self.arrangement_version, 'to_alipay_dict'):
                params['arrangement_version'] = self.arrangement_version.to_alipay_dict()
            else:
                params['arrangement_version'] = self.arrangement_version
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_expired:
            if hasattr(self.gmt_expired, 'to_alipay_dict'):
                params['gmt_expired'] = self.gmt_expired.to_alipay_dict()
            else:
                params['gmt_expired'] = self.gmt_expired
        if self.gmt_invalid_due:
            if hasattr(self.gmt_invalid_due, 'to_alipay_dict'):
                params['gmt_invalid_due'] = self.gmt_invalid_due.to_alipay_dict()
            else:
                params['gmt_invalid_due'] = self.gmt_invalid_due
        if self.gmt_sign:
            if hasattr(self.gmt_sign, 'to_alipay_dict'):
                params['gmt_sign'] = self.gmt_sign.to_alipay_dict()
            else:
                params['gmt_sign'] = self.gmt_sign
        if self.gmt_vald_due:
            if hasattr(self.gmt_vald_due, 'to_alipay_dict'):
                params['gmt_vald_due'] = self.gmt_vald_due.to_alipay_dict()
            else:
                params['gmt_vald_due'] = self.gmt_vald_due
        if self.gmt_vrsn:
            if hasattr(self.gmt_vrsn, 'to_alipay_dict'):
                params['gmt_vrsn'] = self.gmt_vrsn.to_alipay_dict()
            else:
                params['gmt_vrsn'] = self.gmt_vrsn
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.last_moder:
            if hasattr(self.last_moder, 'to_alipay_dict'):
                params['last_moder'] = self.last_moder.to_alipay_dict()
            else:
                params['last_moder'] = self.last_moder
        if self.mark_type:
            if hasattr(self.mark_type, 'to_alipay_dict'):
                params['mark_type'] = self.mark_type.to_alipay_dict()
            else:
                params['mark_type'] = self.mark_type
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.moder_type:
            if hasattr(self.moder_type, 'to_alipay_dict'):
                params['moder_type'] = self.moder_type.to_alipay_dict()
            else:
                params['moder_type'] = self.moder_type
        if self.pd_mark:
            if hasattr(self.pd_mark, 'to_alipay_dict'):
                params['pd_mark'] = self.pd_mark.to_alipay_dict()
            else:
                params['pd_mark'] = self.pd_mark
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.prod_name:
            if hasattr(self.prod_name, 'to_alipay_dict'):
                params['prod_name'] = self.prod_name.to_alipay_dict()
            else:
                params['prod_name'] = self.prod_name
        if self.prod_version:
            if hasattr(self.prod_version, 'to_alipay_dict'):
                params['prod_version'] = self.prod_version.to_alipay_dict()
            else:
                params['prod_version'] = self.prod_version
        if self.ps_code:
            if hasattr(self.ps_code, 'to_alipay_dict'):
                params['ps_code'] = self.ps_code.to_alipay_dict()
            else:
                params['ps_code'] = self.ps_code
        if self.ps_id:
            if hasattr(self.ps_id, 'to_alipay_dict'):
                params['ps_id'] = self.ps_id.to_alipay_dict()
            else:
                params['ps_id'] = self.ps_id
        if self.ps_name:
            if hasattr(self.ps_name, 'to_alipay_dict'):
                params['ps_name'] = self.ps_name.to_alipay_dict()
            else:
                params['ps_name'] = self.ps_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_prod_code:
            if hasattr(self.template_prod_code, 'to_alipay_dict'):
                params['template_prod_code'] = self.template_prod_code.to_alipay_dict()
            else:
                params['template_prod_code'] = self.template_prod_code
        if self.template_prod_version:
            if hasattr(self.template_prod_version, 'to_alipay_dict'):
                params['template_prod_version'] = self.template_prod_version.to_alipay_dict()
            else:
                params['template_prod_version'] = self.template_prod_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArrangementBaseVO()
        if 'app_id' in d:
            o.app_id = d['app_id']
        if 'arrangement_institution_code' in d:
            o.arrangement_institution_code = d['arrangement_institution_code']
        if 'arrangement_name' in d:
            o.arrangement_name = d['arrangement_name']
        if 'arrangement_no' in d:
            o.arrangement_no = d['arrangement_no']
        if 'arrangement_type' in d:
            o.arrangement_type = d['arrangement_type']
        if 'arrangement_version' in d:
            o.arrangement_version = d['arrangement_version']
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_expired' in d:
            o.gmt_expired = d['gmt_expired']
        if 'gmt_invalid_due' in d:
            o.gmt_invalid_due = d['gmt_invalid_due']
        if 'gmt_sign' in d:
            o.gmt_sign = d['gmt_sign']
        if 'gmt_vald_due' in d:
            o.gmt_vald_due = d['gmt_vald_due']
        if 'gmt_vrsn' in d:
            o.gmt_vrsn = d['gmt_vrsn']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'last_moder' in d:
            o.last_moder = d['last_moder']
        if 'mark_type' in d:
            o.mark_type = d['mark_type']
        if 'memo' in d:
            o.memo = d['memo']
        if 'moder_type' in d:
            o.moder_type = d['moder_type']
        if 'pd_mark' in d:
            o.pd_mark = d['pd_mark']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'prod_name' in d:
            o.prod_name = d['prod_name']
        if 'prod_version' in d:
            o.prod_version = d['prod_version']
        if 'ps_code' in d:
            o.ps_code = d['ps_code']
        if 'ps_id' in d:
            o.ps_id = d['ps_id']
        if 'ps_name' in d:
            o.ps_name = d['ps_name']
        if 'status' in d:
            o.status = d['status']
        if 'template_prod_code' in d:
            o.template_prod_code = d['template_prod_code']
        if 'template_prod_version' in d:
            o.template_prod_version = d['template_prod_version']
        return o


