#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniAppPluginInfo import MiniAppPluginInfo


class AlipayOpenMiniInnerversionInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionInfoQueryResponse, self).__init__()
        self._app_version = None
        self._build_source = None
        self._bundle_id = None
        self._create_time = None
        self._description = None
        self._ext_json = None
        self._gmt_modified = None
        self._gray_start_time = None
        self._gray_strategy = None
        self._mini_app_id = None
        self._offline_time = None
        self._package_url = None
        self._plugin_refs = None
        self._reject_reason = None
        self._rollback_time = None
        self._scan_result = None
        self._screen_shot_list = None
        self._shelf_time = None
        self._source_url = None
        self._status = None
        self._template_extra = None
        self._template_version = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def build_source(self):
        return self._build_source

    @build_source.setter
    def build_source(self, value):
        self._build_source = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def ext_json(self):
        return self._ext_json

    @ext_json.setter
    def ext_json(self, value):
        self._ext_json = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def gray_start_time(self):
        return self._gray_start_time

    @gray_start_time.setter
    def gray_start_time(self, value):
        self._gray_start_time = value
    @property
    def gray_strategy(self):
        return self._gray_strategy

    @gray_strategy.setter
    def gray_strategy(self, value):
        self._gray_strategy = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def offline_time(self):
        return self._offline_time

    @offline_time.setter
    def offline_time(self, value):
        self._offline_time = value
    @property
    def package_url(self):
        return self._package_url

    @package_url.setter
    def package_url(self, value):
        self._package_url = value
    @property
    def plugin_refs(self):
        return self._plugin_refs

    @plugin_refs.setter
    def plugin_refs(self, value):
        if isinstance(value, list):
            self._plugin_refs = list()
            for i in value:
                if isinstance(i, MiniAppPluginInfo):
                    self._plugin_refs.append(i)
                else:
                    self._plugin_refs.append(MiniAppPluginInfo.from_alipay_dict(i))
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def rollback_time(self):
        return self._rollback_time

    @rollback_time.setter
    def rollback_time(self, value):
        self._rollback_time = value
    @property
    def scan_result(self):
        return self._scan_result

    @scan_result.setter
    def scan_result(self, value):
        self._scan_result = value
    @property
    def screen_shot_list(self):
        return self._screen_shot_list

    @screen_shot_list.setter
    def screen_shot_list(self, value):
        self._screen_shot_list = value
    @property
    def shelf_time(self):
        return self._shelf_time

    @shelf_time.setter
    def shelf_time(self, value):
        self._shelf_time = value
    @property
    def source_url(self):
        return self._source_url

    @source_url.setter
    def source_url(self, value):
        self._source_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_extra(self):
        return self._template_extra

    @template_extra.setter
    def template_extra(self, value):
        self._template_extra = value
    @property
    def template_version(self):
        return self._template_version

    @template_version.setter
    def template_version(self, value):
        self._template_version = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionInfoQueryResponse, self).parse_response_content(response_content)
        if 'app_version' in response:
            self.app_version = response['app_version']
        if 'build_source' in response:
            self.build_source = response['build_source']
        if 'bundle_id' in response:
            self.bundle_id = response['bundle_id']
        if 'create_time' in response:
            self.create_time = response['create_time']
        if 'description' in response:
            self.description = response['description']
        if 'ext_json' in response:
            self.ext_json = response['ext_json']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'gray_start_time' in response:
            self.gray_start_time = response['gray_start_time']
        if 'gray_strategy' in response:
            self.gray_strategy = response['gray_strategy']
        if 'mini_app_id' in response:
            self.mini_app_id = response['mini_app_id']
        if 'offline_time' in response:
            self.offline_time = response['offline_time']
        if 'package_url' in response:
            self.package_url = response['package_url']
        if 'plugin_refs' in response:
            self.plugin_refs = response['plugin_refs']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
        if 'rollback_time' in response:
            self.rollback_time = response['rollback_time']
        if 'scan_result' in response:
            self.scan_result = response['scan_result']
        if 'screen_shot_list' in response:
            self.screen_shot_list = response['screen_shot_list']
        if 'shelf_time' in response:
            self.shelf_time = response['shelf_time']
        if 'source_url' in response:
            self.source_url = response['source_url']
        if 'status' in response:
            self.status = response['status']
        if 'template_extra' in response:
            self.template_extra = response['template_extra']
        if 'template_version' in response:
            self.template_version = response['template_version']
