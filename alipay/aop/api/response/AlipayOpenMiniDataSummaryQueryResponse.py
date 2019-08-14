#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniDataSummaryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniDataSummaryQueryResponse, self).__init__()
        self._app_pv = None
        self._app_uv = None
        self._avg_stay_time_per_user = None
        self._avg_stay_time_per_visit = None
        self._launch_cnt = None
        self._launch_cnt_dst = None
        self._new_user_cnt = None
        self._share_cnt = None
        self._share_cnt_dst = None
        self._share_user_cnt = None
        self._share_user_cnt_dst = None
        self._user_cnt_30_d = None
        self._user_cnt_7_d = None
        self._user_cnt_dst = None

    @property
    def app_pv(self):
        return self._app_pv

    @app_pv.setter
    def app_pv(self, value):
        self._app_pv = value
    @property
    def app_uv(self):
        return self._app_uv

    @app_uv.setter
    def app_uv(self, value):
        self._app_uv = value
    @property
    def avg_stay_time_per_user(self):
        return self._avg_stay_time_per_user

    @avg_stay_time_per_user.setter
    def avg_stay_time_per_user(self, value):
        self._avg_stay_time_per_user = value
    @property
    def avg_stay_time_per_visit(self):
        return self._avg_stay_time_per_visit

    @avg_stay_time_per_visit.setter
    def avg_stay_time_per_visit(self, value):
        self._avg_stay_time_per_visit = value
    @property
    def launch_cnt(self):
        return self._launch_cnt

    @launch_cnt.setter
    def launch_cnt(self, value):
        self._launch_cnt = value
    @property
    def launch_cnt_dst(self):
        return self._launch_cnt_dst

    @launch_cnt_dst.setter
    def launch_cnt_dst(self, value):
        self._launch_cnt_dst = value
    @property
    def new_user_cnt(self):
        return self._new_user_cnt

    @new_user_cnt.setter
    def new_user_cnt(self, value):
        self._new_user_cnt = value
    @property
    def share_cnt(self):
        return self._share_cnt

    @share_cnt.setter
    def share_cnt(self, value):
        self._share_cnt = value
    @property
    def share_cnt_dst(self):
        return self._share_cnt_dst

    @share_cnt_dst.setter
    def share_cnt_dst(self, value):
        self._share_cnt_dst = value
    @property
    def share_user_cnt(self):
        return self._share_user_cnt

    @share_user_cnt.setter
    def share_user_cnt(self, value):
        self._share_user_cnt = value
    @property
    def share_user_cnt_dst(self):
        return self._share_user_cnt_dst

    @share_user_cnt_dst.setter
    def share_user_cnt_dst(self, value):
        self._share_user_cnt_dst = value
    @property
    def user_cnt_30_d(self):
        return self._user_cnt_30_d

    @user_cnt_30_d.setter
    def user_cnt_30_d(self, value):
        self._user_cnt_30_d = value
    @property
    def user_cnt_7_d(self):
        return self._user_cnt_7_d

    @user_cnt_7_d.setter
    def user_cnt_7_d(self, value):
        self._user_cnt_7_d = value
    @property
    def user_cnt_dst(self):
        return self._user_cnt_dst

    @user_cnt_dst.setter
    def user_cnt_dst(self, value):
        self._user_cnt_dst = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniDataSummaryQueryResponse, self).parse_response_content(response_content)
        if 'app_pv' in response:
            self.app_pv = response['app_pv']
        if 'app_uv' in response:
            self.app_uv = response['app_uv']
        if 'avg_stay_time_per_user' in response:
            self.avg_stay_time_per_user = response['avg_stay_time_per_user']
        if 'avg_stay_time_per_visit' in response:
            self.avg_stay_time_per_visit = response['avg_stay_time_per_visit']
        if 'launch_cnt' in response:
            self.launch_cnt = response['launch_cnt']
        if 'launch_cnt_dst' in response:
            self.launch_cnt_dst = response['launch_cnt_dst']
        if 'new_user_cnt' in response:
            self.new_user_cnt = response['new_user_cnt']
        if 'share_cnt' in response:
            self.share_cnt = response['share_cnt']
        if 'share_cnt_dst' in response:
            self.share_cnt_dst = response['share_cnt_dst']
        if 'share_user_cnt' in response:
            self.share_user_cnt = response['share_user_cnt']
        if 'share_user_cnt_dst' in response:
            self.share_user_cnt_dst = response['share_user_cnt_dst']
        if 'user_cnt_30_d' in response:
            self.user_cnt_30_d = response['user_cnt_30_d']
        if 'user_cnt_7_d' in response:
            self.user_cnt_7_d = response['user_cnt_7_d']
        if 'user_cnt_dst' in response:
            self.user_cnt_dst = response['user_cnt_dst']
