#include <python/Python.h>
#include<iostream>
using namespace std;

int main()
{
	Py_Initialize();              //初始化，创建一个Python虚拟环境
	if (Py_IsInitialized())
	{
		PyObject* pModule = NULL;
		PyObject* pFunc = NULL;
		pModule = PyImport_ImportModule("1");  //参数为Python脚本的文件名
		if (pModule)
		{
			pFunc = PyObject_GetAttrString(pModule, "printlist1");   //获取函数
			//PyEval_CallObject(pFunc, NULL);
			///////////////////////////////////////////////////////////////
			//为指定位置指定参数，定义元组
			PyObject *args1 = PyTuple_New(2);//传入两个参数
			PyObject *arg1 = PyLong_FromLong(100);//C++的long转换为pylong
			//PyObject *arg11 = Py_BuildValue("i", 100);//同上
			PyObject *arg2 = PyLong_FromLong(20);
			PyTuple_SetItem(args1, 0, arg1);
			PyTuple_SetItem(args1, 1, arg2);
			PyObject *pret = PyObject_CallObject(pFunc, args1);
			int res1;
			PyArg_Parse(pret, "i", &res1);//转换返回类型integer
			cout << res1 << endl;
			///////////////////////////////////////////////////

			PyObject* args = Py_BuildValue("(ii)", 28, 103);//给python函数参数赋值,此处为参数赋值为按照默认顺序，效果同上
			PyObject *pRet = PyObject_CallFunction(pFunc, "OO", arg1, arg2);//同下，“O”表示对象为PyObject.几个参数就是几个"O"
			//PyObject* pRet = PyObject_CallObject(pFunc, args);//调用函数
			int res = 0;
			PyArg_Parse(pRet, "i", &res);//转换返回类型
			cout << res << endl;
			////////////////////////////////////////////////////

			/////////////////////////////////////////////////////////
			//list操作
			PyObject*pyParams = PyList_New(0);           //初始化一个列表
			PyList_Append(pyParams, Py_BuildValue("i", 5));//列表添加元素值
			PyList_Append(pyParams, Py_BuildValue("i", 2));
			PyList_Append(pyParams, Py_BuildValue("i", 6));
			PyList_Append(pyParams, Py_BuildValue("i", 8));
			//将列表转换为元组的一个元素之后传入元组作为Python程序的参数
			PyObject*args = PyTuple_New(1);            
			PyTuple_SetItem(args, 0, pyParams);
			//PySet_Add(pyset,key);
			//PySet_Pop(pyset);

			///////////////////////////////////////////////////////////
			/*
			"s"(string) [char *] ：将C字符串转换成Python对象，如果C字符串为空，返回NONE。
            "s#"(string) [char *, int] :将C字符串和它的长度转换成Python对象，如果C字符串为空指针，长度忽略，返回NONE。
            "z"(string or None) [char *] :作用同"s"
     		"z#" (stringor None) [char *, int] :作用同"s#"。
     		"i"(integer) [int] :将一个C类型的int转换成Python int对象。
        	"b"(integer) [char] :作用同"i"。
        	"h"(integer) [short int] ：作用同"i"。
        	"l"(integer) [long int] :将C类型的long转换成Pyhon中的int对象。
        	"c"(string of length 1) [char] ：将C类型的char转换成长度为1的Python字符串对象。
        	"d"(float) [double] :将C类型的double转换成python中的浮点型对象。
        	"f"(float) [float] :作用同"d"。
        	"O&"(object) [converter, anything] ：将任何数据类型通过转换函数转换成Python对象，这些数据作为转换函数的参数被调用并且返回一个新的Python对象，如果发生错误返回NULL。
        	"(items)"(tuple) [matching-items] ：将一系列的C值转换成Python元组。
        	"[items]"(list) [matching-items] ：将一系列的C值转换成Python列表。
        	"{items}"(dictionary) [matching-items] ：将一系类的C值转换成Python的字典，每一对连续的C值将转换成一个键值对。
			*/
			PyObject* index0 = Py_BuildValue("i", 10);
			//或
			int array[4] = {1, 2, 3, 4};
			PyObject* argslist = Py_BuildValue("([i,i,i,i])",1,2,3,4);//[1,2,3,4]此为一个列表
			PyObject* argsdict = Py_BuildValue("({s:i,s:i})", "abc", 123, "def", 456);//{"abc":123,"def","456"}此为一个字典
			PyObject* argstuple = Py_BuildValue("((i,i,i,i))", 23, 12, 12, 1);//(23,12,12,1)此为一个元组
			PyObject* args2= Py_BuildValue("(i,i,i,i)", 23, 12, 12, 1);//此为4个参数
			//PyObject* args2= Py_BuildValue("(iiii)", 23, 12, 12, 1);//此为4个参数
			//PyObject* args2= Py_BuildValue("iiii", 23, 12, 12, 1);//此为4个参数
			PyObject* args3 = Py_BuildValue("(s,s,s,s)", "s", "12", "12", "1");//此为4个参数,格式含义同i
			//PyObject* args3 = Py_BuildValue("ssss", "s", "12", "12", "1");//此为4个参数,格式含义同i
			//PyObject* args3 = Py_BuildValue("(ssss)", "s", "12", "12", "1");//此为4个参数,格式含义同i
			PyObject* args4 = Py_BuildValue("(s)", "hello");//'hello'
			PyObject* args5 = Py_BuildValue("(s#)", "hello",4);//'hell'
			PyObject* ret1=PyObject_CallObject(pFunc, args4);
			int ret[4] = { 0 };
			//PyList_SetItem(obj, index, args);
			//获取列表的值
			int listsize = PyList_Size(ret1);//获取返回列表的大小
			for (int i = 0; i < listsize; i++) {
				PyObject* listItem = PyList_GetItem(ret1, i);//获得返回列表对象的每一项
				cout << PyLong_AsLong(listItem) << " ";//py对象转换为C++对象输出
				Py_DECREF(listItem);
			}
			Py_DECREF(ret1);
			//PyTuple_Size(Obj)
			//PyTuple_SetItem(Obj, index, arg);
			//PyTuple_GetItem(Obj,index)
			//PyDict_Size(Obj)
			//PyDict_SetItem(Obj, index, arg);
			//PyDict_GetItem(Obj,key)
			//PySet_Size(Obj)
			//Py_DECREF()释放py对象
 		}
		else
		{
			printf("导入Python模块失败...\n");
		}
	}
	else
	{
		printf("Python环境初始化失败...\n");
	}
	
	Py_Finalize();
	system("pause");
	return 0;
}
