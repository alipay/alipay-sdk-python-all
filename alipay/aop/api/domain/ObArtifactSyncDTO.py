#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExemptApprovalProcessDetail import ExemptApprovalProcessDetail
from alipay.aop.api.domain.ScanDetail import ScanDetail


class ObArtifactSyncDTO(object):

    def __init__(self):
        self._artifact_fullname = None
        self._artifact_version = None
        self._branch_or_tag = None
        self._build_id = None
        self._commit_id = None
        self._create_time = None
        self._download_url = None
        self._exempt_approval_process_details = None
        self._external_disclosure_process_state = None
        self._external_disclosure_process_url = None
        self._md_5 = None
        self._project_name = None
        self._publisher = None
        self._purpose = None
        self._repo_url = None
        self._scan_details = None
        self._size = None
        self._trigger = None
        self._type = None

    @property
    def artifact_fullname(self):
        return self._artifact_fullname

    @artifact_fullname.setter
    def artifact_fullname(self, value):
        self._artifact_fullname = value
    @property
    def artifact_version(self):
        return self._artifact_version

    @artifact_version.setter
    def artifact_version(self, value):
        self._artifact_version = value
    @property
    def branch_or_tag(self):
        return self._branch_or_tag

    @branch_or_tag.setter
    def branch_or_tag(self, value):
        self._branch_or_tag = value
    @property
    def build_id(self):
        return self._build_id

    @build_id.setter
    def build_id(self, value):
        self._build_id = value
    @property
    def commit_id(self):
        return self._commit_id

    @commit_id.setter
    def commit_id(self, value):
        self._commit_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def exempt_approval_process_details(self):
        return self._exempt_approval_process_details

    @exempt_approval_process_details.setter
    def exempt_approval_process_details(self, value):
        if isinstance(value, list):
            self._exempt_approval_process_details = list()
            for i in value:
                if isinstance(i, ExemptApprovalProcessDetail):
                    self._exempt_approval_process_details.append(i)
                else:
                    self._exempt_approval_process_details.append(ExemptApprovalProcessDetail.from_alipay_dict(i))
    @property
    def external_disclosure_process_state(self):
        return self._external_disclosure_process_state

    @external_disclosure_process_state.setter
    def external_disclosure_process_state(self, value):
        self._external_disclosure_process_state = value
    @property
    def external_disclosure_process_url(self):
        return self._external_disclosure_process_url

    @external_disclosure_process_url.setter
    def external_disclosure_process_url(self, value):
        self._external_disclosure_process_url = value
    @property
    def md_5(self):
        return self._md_5

    @md_5.setter
    def md_5(self, value):
        self._md_5 = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value
    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value
    @property
    def purpose(self):
        return self._purpose

    @purpose.setter
    def purpose(self, value):
        self._purpose = value
    @property
    def repo_url(self):
        return self._repo_url

    @repo_url.setter
    def repo_url(self, value):
        self._repo_url = value
    @property
    def scan_details(self):
        return self._scan_details

    @scan_details.setter
    def scan_details(self, value):
        if isinstance(value, list):
            self._scan_details = list()
            for i in value:
                if isinstance(i, ScanDetail):
                    self._scan_details.append(i)
                else:
                    self._scan_details.append(ScanDetail.from_alipay_dict(i))
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def trigger(self):
        return self._trigger

    @trigger.setter
    def trigger(self, value):
        self._trigger = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.artifact_fullname:
            if hasattr(self.artifact_fullname, 'to_alipay_dict'):
                params['artifact_fullname'] = self.artifact_fullname.to_alipay_dict()
            else:
                params['artifact_fullname'] = self.artifact_fullname
        if self.artifact_version:
            if hasattr(self.artifact_version, 'to_alipay_dict'):
                params['artifact_version'] = self.artifact_version.to_alipay_dict()
            else:
                params['artifact_version'] = self.artifact_version
        if self.branch_or_tag:
            if hasattr(self.branch_or_tag, 'to_alipay_dict'):
                params['branch_or_tag'] = self.branch_or_tag.to_alipay_dict()
            else:
                params['branch_or_tag'] = self.branch_or_tag
        if self.build_id:
            if hasattr(self.build_id, 'to_alipay_dict'):
                params['build_id'] = self.build_id.to_alipay_dict()
            else:
                params['build_id'] = self.build_id
        if self.commit_id:
            if hasattr(self.commit_id, 'to_alipay_dict'):
                params['commit_id'] = self.commit_id.to_alipay_dict()
            else:
                params['commit_id'] = self.commit_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.download_url:
            if hasattr(self.download_url, 'to_alipay_dict'):
                params['download_url'] = self.download_url.to_alipay_dict()
            else:
                params['download_url'] = self.download_url
        if self.exempt_approval_process_details:
            if isinstance(self.exempt_approval_process_details, list):
                for i in range(0, len(self.exempt_approval_process_details)):
                    element = self.exempt_approval_process_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.exempt_approval_process_details[i] = element.to_alipay_dict()
            if hasattr(self.exempt_approval_process_details, 'to_alipay_dict'):
                params['exempt_approval_process_details'] = self.exempt_approval_process_details.to_alipay_dict()
            else:
                params['exempt_approval_process_details'] = self.exempt_approval_process_details
        if self.external_disclosure_process_state:
            if hasattr(self.external_disclosure_process_state, 'to_alipay_dict'):
                params['external_disclosure_process_state'] = self.external_disclosure_process_state.to_alipay_dict()
            else:
                params['external_disclosure_process_state'] = self.external_disclosure_process_state
        if self.external_disclosure_process_url:
            if hasattr(self.external_disclosure_process_url, 'to_alipay_dict'):
                params['external_disclosure_process_url'] = self.external_disclosure_process_url.to_alipay_dict()
            else:
                params['external_disclosure_process_url'] = self.external_disclosure_process_url
        if self.md_5:
            if hasattr(self.md_5, 'to_alipay_dict'):
                params['md_5'] = self.md_5.to_alipay_dict()
            else:
                params['md_5'] = self.md_5
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        if self.publisher:
            if hasattr(self.publisher, 'to_alipay_dict'):
                params['publisher'] = self.publisher.to_alipay_dict()
            else:
                params['publisher'] = self.publisher
        if self.purpose:
            if hasattr(self.purpose, 'to_alipay_dict'):
                params['purpose'] = self.purpose.to_alipay_dict()
            else:
                params['purpose'] = self.purpose
        if self.repo_url:
            if hasattr(self.repo_url, 'to_alipay_dict'):
                params['repo_url'] = self.repo_url.to_alipay_dict()
            else:
                params['repo_url'] = self.repo_url
        if self.scan_details:
            if isinstance(self.scan_details, list):
                for i in range(0, len(self.scan_details)):
                    element = self.scan_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scan_details[i] = element.to_alipay_dict()
            if hasattr(self.scan_details, 'to_alipay_dict'):
                params['scan_details'] = self.scan_details.to_alipay_dict()
            else:
                params['scan_details'] = self.scan_details
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.trigger:
            if hasattr(self.trigger, 'to_alipay_dict'):
                params['trigger'] = self.trigger.to_alipay_dict()
            else:
                params['trigger'] = self.trigger
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ObArtifactSyncDTO()
        if 'artifact_fullname' in d:
            o.artifact_fullname = d['artifact_fullname']
        if 'artifact_version' in d:
            o.artifact_version = d['artifact_version']
        if 'branch_or_tag' in d:
            o.branch_or_tag = d['branch_or_tag']
        if 'build_id' in d:
            o.build_id = d['build_id']
        if 'commit_id' in d:
            o.commit_id = d['commit_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'download_url' in d:
            o.download_url = d['download_url']
        if 'exempt_approval_process_details' in d:
            o.exempt_approval_process_details = d['exempt_approval_process_details']
        if 'external_disclosure_process_state' in d:
            o.external_disclosure_process_state = d['external_disclosure_process_state']
        if 'external_disclosure_process_url' in d:
            o.external_disclosure_process_url = d['external_disclosure_process_url']
        if 'md_5' in d:
            o.md_5 = d['md_5']
        if 'project_name' in d:
            o.project_name = d['project_name']
        if 'publisher' in d:
            o.publisher = d['publisher']
        if 'purpose' in d:
            o.purpose = d['purpose']
        if 'repo_url' in d:
            o.repo_url = d['repo_url']
        if 'scan_details' in d:
            o.scan_details = d['scan_details']
        if 'size' in d:
            o.size = d['size']
        if 'trigger' in d:
            o.trigger = d['trigger']
        if 'type' in d:
            o.type = d['type']
        return o


