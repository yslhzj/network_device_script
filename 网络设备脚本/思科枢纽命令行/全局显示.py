from ..命令行接口 import 全局显示
class C全局显示nv7_0(全局显示.I全局显示):
	"""适用于: 思科nexus9000(v7.0), 浪潮cn8000系列(v7.3), 浪潮cn61108pcv(v7.0)"""
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show startup-config")
		return v输出
	def f显示_当前配置(self):
		v输出 = self.m设备.f执行显示命令("show running-config")
		return v输出
	def f显示_时间(self):
		v命令 = "show clock"
		v输出 = self.m设备.f执行显示命令(v命令)
		from . import 时间
		return 时间.f解析时间(v输出)
	def f显示_设备版本(self):
		return self.fg版本信息()