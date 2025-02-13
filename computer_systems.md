# Computer Systems

## IO buffering

When writing to a slow USB drive with a large writeback cache, it can appear as if a write operation has stalled to many processes. This is most apparent as a user when copying a file with some progress bar which appears stalled even though there is activity. In this case you can view the writeback cache status as follows:

```
watch "cat /proc/meminfo | grep -i writeback"
```
