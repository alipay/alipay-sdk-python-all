#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAgentVersionDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAgentVersionDetailQueryResponse, self).__init__()
        self._app_logo = None
        self._app_name = None
        self._app_version = None
        self._audit_reason = None
        self._bundle_id = None
        self._gmt_apply_audit = None
        self._gmt_audit_end = None
        self._gmt_create = None
        self._gmt_offline = None
        self._gmt_online = None
        self._status = None
        self._version_desc = None

    @property
    def app_logo(self):
        return self._app_logo

    @app_logo.setter
    def app_logo(self, value):
        self._app_logo = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def audit_reason(self):
        return self._audit_reason

    @audit_reason.setter
    def audit_reason(self, value):
        self._audit_reason = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def gmt_apply_audit(self):
        return self._gmt_apply_audit

    @gmt_apply_audit.setter
    def gmt_apply_audit(self, value):
        self._gmt_apply_audit = value
    @property
    def gmt_audit_end(self):
        return self._gmt_audit_end

    @gmt_audit_end.setter
    def gmt_audit_end(self, value):
        self._gmt_audit_end = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_offline(self):
        return self._gmt_offline

    @gmt_offline.setter
    def gmt_offline(self, value):
        self._gmt_offline = value
    @property
    def gmt_online(self):
        return self._gmt_online

    @gmt_online.setter
    def gmt_online(self, value):
        self._gmt_online = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def version_desc(self):
        return self._version_desc

    @version_desc.setter
    def version_desc(self, value):
        self._version_desc = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAgentVersionDetailQueryResponse, self).parse_response_content(response_content)
        if 'app_logo' in response:
            self.app_logo = response['app_logo']
        if 'app_name' in response:
            self.app_name = response['app_name']
        if 'app_version' in response:
            self.app_version = response['app_version']
        if 'audit_reason' in response:
            self.audit_reason = response['audit_reason']
        if 'bundle_id' in response:
            self.bundle_id = response['bundle_id']
        if 'gmt_apply_audit' in response:
            self.gmt_apply_audit = response['gmt_apply_audit']
        if 'gmt_audit_end' in response:
            self.gmt_audit_end = response['gmt_audit_end']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_offline' in response:
            self.gmt_offline = response['gmt_offline']
        if 'gmt_online' in response:
            self.gmt_online = response['gmt_online']
        if 'status' in response:
            self.status = response['status']
        if 'version_desc' in response:
            self.version_desc = response['version_desc']
